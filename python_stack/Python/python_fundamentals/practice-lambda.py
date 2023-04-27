# lambda
#def increaseBy2(arr, func):
#    for count in range(len(arr)):
#        arr[count] = func(arr[count])
#    return arr

#print(increaseBy2([1,2,3,4], lambda x: 2 + x))

#def divideBy2(arr, lamb):
#    for count in range(len(arr)):
#        arr[count] = lamb(arr[count])
#    return arr
#print(divideBy2([1, 2, 3, 4], lambda x: x / 2))

# map()
arr = [1, 2, 3, 4]
print(list(map(lambda x: x*2, arr)))
