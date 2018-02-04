'''Bucket sort is similar to radix sort, the only difference is
1) we distribute only once
2) we need to create a container and
3)within container we need to sort all the elemets
'''

import Queue
from Queue import PriorityQueue

def bucketSort(Arr, n=5):
    maxVal = max (Arr)
    minVal = min(Arr)
    count = (maxVal-minVal)/5

    #put values in priority queue/dictionary
    q = Queue.PriorityQueue()
    for i in range(len(Arr)):
        if (Arr[i]<count):
            q.put(0,Arr[i])
        elif Arr[i] in range (count, 2*count):
            q.put(1,Arr[i])
        elif Arr[i] in range (2*count, 3*count):
            q.put(2,Arr[i])
        elif Arr[i] in range(3 * count, 4 * count):
            q.put(3, Arr[i])
        else:
            q.put(4,Arr[i])

    print Arr, count, 2* count
    while not q.empty():
        val = q.get()
        print val

bSort= [170, 45, 801, 90, 802, 24, 2, 66]
# print 'Unsorted:', bSort
bucketSort(bSort)
# print bSort