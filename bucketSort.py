'''Bucket sort as we put elements in bucket we need to sort it as well
so first get an element then insert in the appropriate place in the bucket
'''

import time
import random

def sort_bucket(A):  #insertion sort
    size = len(A)
    for i in range(1, size):
        j = i-1
        temp = A[i]
        while j in range(0,size):
            if (temp<A[j]):
                A[j+1]=A[j]
                j-=1
            else: break
        A[j+1] = temp

#----------------------------------------------

def bucketSort(Arr, n=5):
    maxVal = max (Arr)
    minVal = min(Arr)
    bucket = 5
    count = (maxVal-minVal)/bucket
    temp_Arr = []

    #put values in priority queue/dictionary
    for i in range(len(Arr)):
        if (Arr[i]<count):
            temp_Arr.append((0,Arr[i]))
            sort_bucket (temp_Arr)
        elif Arr[i] in range (count, 2*count):
            temp_Arr.append ((1, Arr[i]))
            sort_bucket(temp_Arr)
        elif Arr[i] in range (2*count, 3*count):
            temp_Arr.append ((2, Arr[i]))
            sort_bucket(temp_Arr)
        elif Arr[i] in range(3 * count, 4 * count):
            temp_Arr.append ((3, Arr[i]))
            sort_bucket(temp_Arr)
        else:
            temp_Arr.append ((4, Arr[i]))
            sort_bucket(temp_Arr)

    #pop elements according to the bucket they are in
    temp_Arr= sorted(temp_Arr, key=lambda x: (x[0]))
    Arr = [i[1] for i in temp_Arr]
    return Arr

# bSort= [800,170, 45, 90, 24, 2,855, 900, 605, 66, 801]
# print 'Unsorted:', bSort
# bSort= bucketSort(bSort)
# print bSort

#
start = time.time()
for j in range(100): # loop 100 times
    bSort = []
    for i in range(10000):  # elements in array
        bSort.append(random.randrange(0,1000))
    bucketSort(bSort)
end = time.time()
t_time =(end - start)

print 'Bucket time:',t_time