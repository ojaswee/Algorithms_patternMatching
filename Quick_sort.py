# Quick sort is very effective sorting technique
# most of the programs use this type of sorting when we call the sort function

def quick_sort(Arr):
    partition_qS(Arr,0,len(Arr)-1)

def partition_qS(Arr,left, right):
    current = left
    pivot = Arr[right]
    wall = left -1
    r = right
    while (current<r):
        if (Arr[current]<=pivot):
            wall = wall+1
            current =current+1
        if (Arr[current]>pivot):
            Arr[r]= Arr[current]
            r= r-1
            Arr[r]= pivot
        partition_qS(Arr,left,wall)
        partition_qS(Arr,wall+1,right)

# Entry point for program execution
A = [3, 1, 9, 0, 12, 90, 45]
quick_sort(A)
print A