# Quick sort is very effective sorting technique
# most of the programs use this type of sorting when we call the sort function
# We do all the sorting in same array and we DONOT create another array

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


# ----------------------Merge Sort -----------------
# in merge sort we first divide the array into individual elements
# compare this individual items and store then n temporary arrays

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

# Code for merge sort

def mergesort(Arr):
    # First partition array into individual elements
    size = len(Arr)
    if size <= 1:
        return Arr
    else:
        mid = size/2
        left = mergesort(Arr[:mid])
        right = mergesort(Arr[mid:])
    return merge(left, right)

# ---------------- Entry point for program execution
qS = [3, 1, 9, 0, 12, 90, 45, 65]
print 'Unsorted Array:', qS
quick_sort(qS)
print 'Quick Sort:', qS

mS = [3, 1, 9, 0, 12, 90, 45, 65]
# print 'Merge Sort:'
mS = mergesort(mS)
print 'Merge Sort:',mS