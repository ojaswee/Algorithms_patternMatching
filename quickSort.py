# Quick sort is very effective sorting technique
# most of the programs use this type of sorting when we call the sort function
# We do all the sorting in same array and we DONOT create another array
# Space complexity: O(log(n))
# Time Complexity: O(n log(n))    Worst: O(n^2)

import time
import random
import sys
sys.setrecursionlimit(100000000)

def quick_sort(Arr):
    partition_qS(Arr,0,len(Arr)-1)

def partition_qS(Arr,left, right):
    lower = left
    pivot = Arr[left]
    upper = right
    while (lower<upper):
        while pivot<Arr[upper] and lower < upper:
            upper -= 1
        if (pivot>Arr[upper]):
            Arr[lower] = Arr[upper]
            lower += 1
        while (pivot>= Arr[lower]) and lower < upper:
            lower +=1
        if (pivot< Arr[lower]):
            Arr[upper]= Arr[lower]
            upper -=1

    Arr[lower] = pivot
    if (left<lower-1):
        partition_qS(Arr,left,lower-1)
    if (upper+1 < right):
        partition_qS(Arr, upper+1,right)



# Entry point for program execution
qS = [3, 1, 9, 0, 12, 90, 45,65]
quick_sort(qS)
print 'Quick Sort:', qS

#For sorting algorithm comparison
# qstart = time.time()
#
# for j in range(100): # loop 100 times
#     qS= []
#     for i in range(50000):  # elements in array
#         qS.append(random.randrange(0,100000))
#     quick_sort(qS)
#
# qend = time.time()
# t_time= (qend - qstart)
# print 'Quick Sort time:',t_time




