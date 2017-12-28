# basic sorting in python

#bubble sort
def bubbleSort(arr):
    size = len(arr)
    for j in range( size-1):
        for i in range(size-1):
            if (arr[i]>arr[i+1]):
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
    return arr

#selection sort
def selectionSort(arr):
    size = len(arr)
    for j in range (size):
        minIndex = j
        for i in range (j+1,size):
            if (arr[minIndex]> arr[i]):
                minIndex = i
                #print arr[minIndex]
        if (minIndex != j):
            temp = arr[j]
            arr[j]= arr[minIndex]
            arr[minIndex] = temp
    return arr


sort = [3, 6, 1, 0, 11, 67, 9, 5, 52]
print 'Given:', sort
bubble = bubbleSort(sort)
print 'Bubble:',bubble

sort = [3, 6, 1, 0, 11, 67, 9, 5, 52]
selection =selectionSort(sort)
print 'Selection:',selection