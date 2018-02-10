'''
Heap sort is useful when we are concerned about the memory usage during sorting
Quick and merge sort use recursive method so they use more space then heap sort
To do ascending heap sort we have to first create a max heapify.
Max heapify has two children similar to complete binary search. First level
has largest element, then second level has smaller elements then level and so on
for example:  Max heapify of  {2,8,5,3,9,1} will be
            9
         /    \
        8      5
      /  \    /
    3     2  1
We only heapify first part of array because right half is only going to have children
    1) After this we replace 1 with 9.
    2) detach 9 and continue with remaining elements
    3) now re-create max heapify from this tree
Number of nodes each layer has is 2^(n-1)
'''

import time
import random

def swap (Arr, m, n):
    temp = Arr[m]
    Arr[m]= Arr[n]
    Arr[n]= temp

def heapSort(Arr):
    size = len(Arr)
    # only iterate to first half of array
    for i in range((size-1)/2,-1,-1):
        heapify(Arr,i,size)
    for i in range (size-1,-1,-1):
        swap(Arr,0, i)
        heapify(Arr, 0, i)
    # print Arr

def heapify(Arr, i, size):
    temp = Arr[i]
    child = i * 2
    while (child<size):
        if (child+1 < size and Arr[child]<Arr[child+1]):
            child = child+1
        if (temp < Arr[child]):
            Arr[i] = Arr[child]
            i = child
            child = child * 2
        else: break
    Arr[i]= temp
    # print Arr


# heapArr= [3,10,5,2,6,8]
# print 'Unsorted:', heapArr
# heapSort(heapArr)
# print 'Heap Sort:', heapArr

start = time.time()
for j in range(100): # loop 100 times
    heapArr = []
    for i in range(50000):  # elements in array
        heapArr.append(random.randrange(0,1000000))
    heapSort(heapArr)

end = time.time()
t_time =(end - start)
print 'Heap time:',t_time

