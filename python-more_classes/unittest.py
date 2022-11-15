import unittest

from class_test import CTest


testObj = CTest()

class Tests(unittest.TestCase):
    def test_1(self):
        testObj.suma_para()
        self.assertTrue()
        
        
if __name__ == '__main__':
    unittest.main()