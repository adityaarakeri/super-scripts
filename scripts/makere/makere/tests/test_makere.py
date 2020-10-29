from makere.makere import Makere
import re
import unittest 

class TestMakere(unittest.TestCase):

    def setUp(self):
        self.o1 = Makere(['abc', 'xyz'])
        self.o2 = Makere(r'E:\pplprhr\makere\makere\tests\test_file.txt')

    
    def test_find_stem(self):
        res  = self.o1._find_stem()
        self.assertEqual(res, [])

        res = self.o2._find_stem()
        self.assertEqual(res, ['http', '://www.lifewire.com/', '-google-'])

    def test_to_list(self):
        res  = self.o1._to_lists()
        self.assertEqual(res, [[['a', 'b', 'c']], [['x','y', 'z']]])

        # res  = self.o2._to_lists()
        # self.assertEqual(res, [[['a', 'b', 'c']], [['x','y', 'z']]])

    def test_compress(self):
        self.o1._compress()
        self.assertEqual(self.o1.processedWords, [[['([a-z])+']], [['([a-z])+']]])

        # self.o2._compress()
        # self.assertEqual(self.o2.processedWords, [[['a', 'b', 'c']], [['x','y', 'z']]])

    def test_make(self):
        #res  = self.o1.make()
        # self.assertEqual(res, ['abc', 'xyz'])

        res  = self.o2.make()
        p = re.compile(res)

        print res

        for wrd in self.o2.words:
            self.assertTrue(re.match(p, wrd))



        # self.assertEqual(res, ['abc', 'xyz'])

if __name__ == '__main__':
    unittest.main()