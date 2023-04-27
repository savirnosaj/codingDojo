# Functions Basic II

# 1. Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number
# (as lists 'zero'th element) down to 0 (as the last element).
# For example countDown(5) should return [5,4,3,2,1,0].

#def countDown(num):
#    list = []
#    while num >= 0:
#        list.append(num)
#        num -= 1
#    return list

#print(countDown(5))

# 2. Print and Return - Your function will receive a list with two numbers.
# Print the first value, and return the second.

#def printNreturn(arr):
#    print("Printing first value: " + str(arr[0]))
#    return arr[1]

#print("Printing returned value: " + str(printNreturn([11, 200])))

# 3. First Plus Length - Given a list, retun the sum of the firt value in the list,
# plus the list's length.

#def firstPlusLength(arr):
#    print("First value in list is: " + str(arr[0]))
#    print("List's length is: " + str(len(arr)))
#    return(arr[0] + len(arr))

#print("Total is: " + str(firstPlusLength([14,2])))

# 4. Values Greater than Second - Write a function that accepts a list,
# and returns a new list with the list values that are greater than its 2nd value.
# Print how many values this is.  If the list is only one element long,
# have the function return False.

#def valuesGreaterThanSecond(arr):
#    newArr = []
#    for count in range(len(arr)):
#        if arr[count] > arr[1]:
#            newArr.append(arr[count])
#        else:
#            continue
#    if len(newArr) < 2:
#        return False
#    else:
#        return newArr

#print(valuesGreaterThanSecond([3, 1, 11, 10, 0]))

# 5.This Length, That Value - Write a function called lengthAndValue which accepts two parameters,
# size, and value. This function should take two numbers and return a list of length size containing
# only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

#def lengthAndValue(size, value):
#    arr = []
#    while size > 0:
#        arr.append(value)
#        size -= 1
#    return arr

#print(lengthAndValue(4, 7))
