import unittest
from addFirstTwo import *

class TestAddFirstTwo(unittest.TestCase):
    def test_correct_addition(self):
        self.assertEqual(addFirstTwo([3,5,7]), 8)
        self.assertEqual(addFirstTwo([1,2,5]), 3)

    def test_wrong_addition(self):
    	self.assertRaises(IndexError, addFirstTwo([1]))

if __name__ == '__main__':
	unittest.main()