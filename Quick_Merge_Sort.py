# Quick sort is very effective sorting technique
# most of the programs use this type of sorting when we call the sort function

def quick_sort(Arr):
    partition_qS(Arr,0,len(Arr)-1)

def partition_qS(Arr,left, right):
    lower = left
    pivot = Arr[left]
    upper = right
    while (lower<upper):
        while pivot<Arr[upper] and lower < upper:
            upper = upper-1
        if (pivot>A[upper]):
            Arr[lower] = Arr[upper]
            lower= lower+1
        while (pivot>= Arr[lower]) and lower < upper:
            lower =lower+1
        if (pivot< Arr[lower]):
            Arr[upper]= Arr[lower]
            upper = upper - 1

    Arr[lower] = pivot
    if (left<lower-1):
        partition_qS(Arr,left,lower-1)
    if (upper+1 < right):
        partition_qS(Arr, upper+1,right)


#----------------------Merge Sort -----------------
def merge_Sort(Arr):
    partition_mS(Arr, 0, len(Arr))

def partition_mS(Arr, left, right):
    print Arr


#---------------- Entry point for program exeution
A = [3, 1, 9, 0, 12, 90, 45,65]
print 'Unsorted Array:', A
quick_sort(A)
print 'Quick Sort:', A

# A = [3, 1, 9, 0, 12, 90, 45]
# print 'Merge Sort:'
# merge_Sort(A)