# ----------------------Merge Sort -----------------
# in merge sort we first divide the array into individual elements
# compare this individual items and store them in new arrays
# Space complexity: O(n)
# Time Complexity: O(n log(n))

import time
import random
import sys
sys.setrecursionlimit(100000000)

def merge(a,b):
    # create a new List
    myList = []
    countA, countB = len(a), len(b)
    while countA> 0 and countB> 0:
        if a[0] < b[0]:
            myList.append(a[0])
            a.remove(a[0])
            countA -=1
        else:
            myList.append(b[0])
            b.remove(b[0])
            countB -=1
    if countA == 0:
        myList += b
    else:
        myList += a
    return myList

# First partition array into individual elements
def mergesort(Arr):
    size = len(Arr)
    if size <= 1:
        return Arr
    else:
        mid = size/2
        left = mergesort(Arr[:mid])
        right = mergesort(Arr[mid:])
    return merge(left, right)


# Entry point for program execution
mS = [3, 1, 9, 0, 12, 90, 45, 65]
mS = mergesort(mS)
print 'Merge Sort:',mS


# start = time.time()
# for j in range(100): # loop 100 times
#     mS = []
#     for i in range(50000): # elements in array
#         mS.append(random.randrange(0,1000000))
#     mS = mergesort(mS)
#
# end = time.time()
# t_time =(end - start)
# print 'Merge Time:',t_time