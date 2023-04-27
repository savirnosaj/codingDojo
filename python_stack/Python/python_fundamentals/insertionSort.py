# Insertion Sort
# Execute insertion sort

def insertionSort(arr):
    for count in range(1, len(arr)):
        temp = count #temp will reset through each iteration
        while  temp > 0 and arr[temp - 1] > arr[temp]: # will have indexerror if try to go beyond 0 and checking if index before is greater
            arr[temp], arr[temp - 1] = arr[temp - 1], arr[temp] # then swap until index value -1 has lower value
            temp = temp - 1 # check all the way until first index value as long as index value is less than index-1

    return arr

print(insertionSort([6,5,3,1,8,7,2,4]))
