# For Loop Basic II

# Imports
import random

# 1.Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big".
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

#def biggieSize(arr):
#    for count in range(len(arr)):
#        if arr[count] > -1:
#            arr[count] = "big"
#        else:
#            continue
#    return arr

#print(biggieSize([0, -7, 5, 4, -1]))

# 2. Count Positives - Given an array of numbers, create a function to replace last value with number of positive values.
# Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
# (Note that zero is not considered to be a positive number).

#def countPositives(arr):
#    for count in range(len(arr)):
#        if count == (len(arr) - 1):
#            arr[count] = random.randrange(0, 10)
#        else:
#            continue
#    return arr

#print(countPositives([-1, 1, 1, 15, 8]))

# 3. Sum Total - Create a function that takes an array as an argument and returns the sum of all the values in the array.
# For example sumTotal([1,2,3,4]) should return 10

#def sumTotal(arr):
#    sum = 0

#    for count in range(len(arr)):
#        sum += arr[count]

#    return sum

#print(sumTotal([1, 2, 3, 4]))

# 4. Average - Create a function that takes an array as an argument and returns the average of all the values in the array.
# For example multiples([1,2,3,4]) should return 2.5

#def average(arr):
#    sum = 0

#    for count in range(len(arr)):
#        sum += arr[count]

#    sum /= len(arr)
#    return sum

#print(average([1, 2, 3, 4]))

# 5. Length - Create a function that takes an array as an argument and returns the length of the array.
# For example length([1,2,3,4]) should return 4

#def length(arr):
#    return len(arr)

#print(length([1, 2, 3, 4, 5]))

# 6. Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.
# If the passed array is empty, have the function return false.
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    if len(arr) == 0:
        return False
    else:
        max = arr[0]
        for count in range(len(arr)):
            if arr[count] < max:
                max = arr[count]
            else:
                continue
        return max

#print(minimum([1, 2, 3, 4, 0]))
#print(minimum([-1, -4, -2, -3]))
#print(minimum([]))

# 7. Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.
# If the passed array is empty, have the function return false.
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

#def maximum(arr):
#    if len(arr) == 0:
#        return False
#    else:
#        max = arr[0]
#        for count in range(len(arr)):
#            if arr[count] > max:
#                max = arr[count]
#            else:
#                continue
#        return max

#print(maximum([1, 2, 5, 3, 4]))
#print(maximum([-1, -2, -3, 0]))
#print(maximum([]))

# 8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the:
# - sumTotal, - average, - minimum, - maximum and - length of the array.

#def ultimateAnalyze(arr):
#    result = {}
#    sum = 0
#    avg = 0
#    min = arr[0]
#    max = 0

#    for count in range(len(arr)):
#        sum += arr[count]
         
#        if arr[count] < min:
#            min = arr[count]
#        elif arr[count] > max:
#            max = arr[count]
#        else:
#            continue

#    avg = (sum / len(arr))
#    result['sum'] = sum
#    result['average'] = avg
#    result['minimum'] = min
#    result['maximum'] = max
    #print(result['sum'])

#    return result

#print(ultimateAnalyze([1, 2, 3, 4]))

# 9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.
# Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1].
# This challenge is known to appear during basic technical interviews.

def reverseList(arr):
    left = 0
    right = (len(arr) - 1)

    for count in range(len(arr)):
        if left < right:
            temp = arr[0]
            arr[count] = arr[right]
            left += 1
            temp = left
            arr[right] = temp
            right -= 1
        else:
            continue
    return arr

result = reverseList([1,2,3,4])
print(result)
