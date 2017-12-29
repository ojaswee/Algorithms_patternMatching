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
    print 'Bubble sort:', arr

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
    print 'Selection sort:', arr

#insertion sort
def insertionSort(arr):
    size = len(arr)
    for i in range(0,size-1):
        minValue=arr[i]
        minIndex = i
        while minIndex > 0 and arr[minIndex - 1] > minValue:
            arr[minIndex] = arr[minIndex - 1]
            minIndex = minIndex - 1
        arr[minIndex] = minValue
    print 'Insertion sort:', arr

# Entry point for program execution
sortB = [3, 6, 1, 0, 11, 67, 9, 5, 52]
print 'Given:', sortB
bubbleSort(sortB)

sortS = [3, 6, 1, 0, 11, 67, 9, 5, 52]
selectionSort(sortS)

sortI = [3, 6, 1, 0, 11, 67, 9, 5, 52]
insertionSort(sortI)
