import unittest
from makere.helper import (
    contiguous_to_plus,
    generate_pattern_from_letter,
    union,
    concat,
    OPTIONAL,
    CHOICE)

class TestHelper(unittest.TestCase):

    def test_contiguous_to_plus(self):
        # self.assertEqual( contiguous_to_plus(['a', 'b', 'c','a', 'b', 'c','d']) , ['abc+', 'd'] )
        # self.assertEqual( contiguous_to_plus(['a', 'b']) , ['a', 'b'] )
        print contiguous_to_plus(['[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]',\
             '-', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '-', '[a-z]', '[a-z]', \
                 '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '-', '[a-z]',\
                      '[a-z]', '[a-z]', '[a-z]', '-', '[a-z]', '[a-z]', '[a-z]', '[a-z]', \
                          '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]',\
                               '[a-z]', '-', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]', '[a-z]'])
        
    def test_generate_pattern_from_letter(self):
        self.assertEqual( generate_pattern_from_letter('a'), '[a-z]')
        self.assertEqual( generate_pattern_from_letter('B'), '[A-Z]')
        self.assertEqual( generate_pattern_from_letter('9'), '[0-9]')
        self.assertEqual( generate_pattern_from_letter('-'), '-')

    def test_union(self):
        # self.assertEqual( union(['a'], ['b']) , [ 'a', ('|',), 'b'] )
        # self.assertEqual( union(['a'], []) , ['a', ('?',)] )
        # self.assertEqual( union(['a', 'b', ], ['a', 'b']) , ['a', 'b'])
        # self.assertEqual( union(['a', 'b', ], ['a', 'b', 'c']) , ['a', 'b', ('|',), 'a', 'b', 'c'])
        #self.assertEqual( union(['a', 'b', ('|',), 'a', 'b', 'c'], ['a', 'b']) , ['a', 'b', ('|',), 'a', 'b', 'c'])
        # self.assertEqual( union(['a', 'b', ('?',), ('|',), 'a', 'b', 'c'], ['a', 'b']) , ['a', 'b', ('?',), ('|',), 'a', 'b', 'c'])
        # self.assertEqual( union(['a', 'b', ('?',), ('|',), 'a', 'b', 'c'], ['a', 'b', 'c']) , ['a', 'b', ('?',), ('|',), 'a', 'b', 'c'])
        self.assertEqual( union(['a', OPTIONAL], []), ['a', OPTIONAL] )

    def test_concat(self):
        input = ['http',\
                    ['s', ('?',)],\
                    '://www.lifewire.com/',\
                    ['(([a-z])+-)+', '([a-z])+'],\
                    '-google-',\
                    ['([0-9])+', ('|',), '([a-z])+', '-', '([0-9])+']                ]

        self.assertEqual( concat(input), '^http((s)?)://www.lifewire.com/((([a-z])+-)+([a-z])+)-google-((([0-9])+)|(([a-z])+-([0-9])+))$' )


if __name__ == "__main__":
    unittest.main()
