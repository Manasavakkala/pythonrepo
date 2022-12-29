import math
import unittest
class testmath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math.add(10,10),20)
        self.assertEqual(math.add(10.2,10.2),20.4)
    def test_sub(self):
        self.assertEqual(math.sub(10,5),10)

if __name__ =="__main__":
    unittest.main()


