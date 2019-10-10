from makere.reader import Reader
import unittest 

class TestReader(unittest.TestCase):

    def setUp(self):
        self.r1 = Reader(['a', 'b'])
        self.r2 = Reader(r'E:\pplprhr\makere\makere\tests\test_file.txt')

    def test_read(self):
        res  = self.r1.read()
        self.assertEqual(res, ['a', 'b'])

        res = self.r2.read()
        self.assertIsInstance(res, list)

if __name__ == '__main__':
    unittest.main()