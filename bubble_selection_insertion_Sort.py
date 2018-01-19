
#Bubble is basic sorting algorithm which sorts by
#conparing two consecutive elements in an array

def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y

def bubble(B):
    size = len(B)
    for i in range(size):
        #in bubble sort with ascending order max element is sorted first
        #hence we dont need to reach size we an reach (size-1) - i
        for j in range(size-i-1):
            if (B[j]>B[j+1]):
                B[j],B[j+1]=swap(B[j],B[j+1])
    print 'Bubble sort:', B

#Selection sort first finds min value
# then we look in the array if we find another value less then
# current min we swap these values
def selection(A):
    size = len(A)
    for i in range (size):
        for j in range (i+1,size):
            if (A[i]>A[j]):
                A[i], A[j] = swap(A[i], A[j])
    print 'Selection Sort:',A

#Insertion sort is better then then bubble and selection sort
#Insertion sort looks at an element
# if we have only one element it is always sorted so we start with
# comparing 2 values first select first element
# compare if this element is greater then values in the array
# if it is smaller then a value insert at right position

def insertion(A):
    size = len(A)
    j = 0
    for i in range(1, size):
        temp = A[i]
        for j in range(i-1,-2,-1):
            if (temp<A[j]):
                A[j+1]=A[j]
            else: break
        A[j+1] = temp
    print 'Insertion Sort:',A


# Entry point for program execution
bub = [3, 1, 9, 0, 12, 90, 45]
bubble(bub)

select = [3, 1, 9, 0, 12, 90, 45]
selection(select)

insert = [3, 1, 9, 0, 12, 90, 45]
insertion(insert)