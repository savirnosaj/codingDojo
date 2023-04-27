# Selection Sort

# Execute selection sort
def selectionSort(arr):
    for count in range(len(arr)):
        for subcount in range(len(arr) - 1):
            temp = arr[subcount]
            if arr[subcount] < arr[count]:
                temp = arr[count]
                arr[count] = arr[subcount]
                arr[subcount] = temp
            else:
                continue
                

    return arr

print(selectionSort([3,1,5,2,6,8,4,7,9]))
