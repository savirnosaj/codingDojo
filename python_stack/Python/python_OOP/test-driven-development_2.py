import unittest

def add(self, *args):
    for count in args:
        self += count
    return self

class findTotal(unittest.TestCase):
    def testOne(self):
        self.assertEqual(add(2,5,1), 8)

if __name__ == '__main__':
    unittest.main()
