# Import the python testing framework
import unittest

# METHODS

#def reverseList(arr):  #DONE
#    left = 0
#    right = len(arr) - 1
#    temp = arr[left]
#    while left < right:                     # [1000,100,10,1]
#        arr[left] = arr[right]              # temp = 100
#        arr[right] = temp                   # [1,10,100,1000]
#        left += 1                           # left = 2 | right = 1
#        right -= 1
#        temp = arr[left]
#    return arr

#def change(num): # DONE
#    arr = []
#    count = 0
#    while num > 0:
#        while num >= 25:
#            count += 1
#            num -= 25
#        arr.append(count)
#        count = 0
#        while num >= 10:
#            count += 1
#            num -= 10
#        arr.append(count)
#        count = 0
#        while num >= 5:
#            count += 1
#            num -= 5
#        arr.append(count)
#        count = 0
#        while num > 0:
#            count += 1
#            num -= 1
#        arr.append(count)
#        print(arr)
#    return arr

#def polinCheck(str): # DONE
#    word = ""
#    strLen = (len(str) - 1)
#    while strLen > -1:
#        word += str[strLen]
#        strLen -= 1
#    return word

#def factorial(num):
#    if num == 1:
#        return num
#    else:
#        return (num * factorial(num - 1))

def fib(num):
    if num <= 1:
        return num
    else:
        return(fib(num-2) + fib(num-1))     #[]

class isFib(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fib(4), 3)
    def testTwo(self):
        self.assertEqual(fib(5), 5)
    def testThree(self):
        self.assertEqual(fib(7), 13)
    def testFour(self):
        self.assertEqual(fib(6), 8)

#class isFactorial(unittest.TestCase):
#    def testONE(self):
#        self.assertEqual(factorial(5), 120)

#    def testTWO(self):
#        self.assertEqual(factorial(7), 5040)

#    def testTHREE(self):
#        self.assertEqual(factorial(4), 24)

#class isPolindrome(unittest.TestCase):
#    def testOne(self):
#        self.assertEqual(polinCheck("racecar"), "racecar")

#    def testTwo(self):
#        self.assertEqual(polinCheck("mom"), "mom")

#    def testThree(self):
#        self.assertEqual(polinCheck("ileana"), "level")

#class reversedTrue(unittest.TestCase):
#    def testONE(self):
#        self.assertEqual(reverseList([1,3,5]), [5,3,1])

#    def testTWO(self):
#        self.assertEqual(reverseList([1000,100,10, 1]), [1,10,100,1000])

#    def testTHREE(self):
#        self.assertEqual(reverseList([50,77,152]), [152,77,50])

#    def testFOUR(self):
#        self.assertEqual(reverseList([48,48,48]), [48,48,48])

#class coin(unittest.TestCase):
#    def testOne(self):
#        print("Running test ONE")
#        self.assertEqual(change(87), [3,1,0,2])

#    def testTwo(self):
#        print("Running test TWO")
#        self.assertEqual(change(92), [3,1,1,2])

#    def testThree(self):
#        print("Running test THREE")
#        self.assertEqual(change(100), [4,0,0,0])

#    def testFour(self):
#        print("Running test FOUR")
#        self.assertEqual(change(41), [1,1,1,1])

if __name__ == '__main__':
    unittest.main()
