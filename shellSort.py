'''
Shell sort is modification to insertion sort
we just compare 2 elements in a gap then rearrange them
Time complexity = O(n^2)
'''

import time
import random

def shellSort(Arr):
    shell_Array(Arr,(len(Arr))/2)

def shell_Array(Arr, gap):
   i = 0
   # for first iteration space = 0 + gap = gap
   space = gap
   while ( space<=len(Arr)-1):
        if Arr[i]>Arr[space]:
            temp = Arr[i]
            Arr[i]= Arr[space]
            Arr[space]= temp
            # print Arr
        i+=1
        space = i + gap

   if gap>0:
       shell_Array(Arr, gap/2)

# shell=[12, 13, 42, 103, 89, 8, 11, 19]
# print 'Unsorted Array:', shell
# shellSort(shell)
# print 'Shell Sort:', shell


start = time.time()
for j in range(100): # loop 100 times
    shell = []
    for i in range(50000):  # elements in array
        shell.append(random.randrange(0,1000000))
    shellSort(shell)
end = time.time()
t_time =(end - start)
print 'Shell time:',t_time