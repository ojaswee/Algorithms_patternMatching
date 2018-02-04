'''
In Radix Sorting is only used to sort numbers
First sort the number by unit digit then tens then hundreds and so on
This soring uses single Linked List
'''
from llist import sllist,sllistnode

def radixSort(Arr):
    #find max value in the array
    maxVal = max(Arr)
    digits = len(str(maxVal))  # find total digits in the max value
    sll = sllist()
    for i in range (0,digits):
        distribute(Arr,i, sll)
        collect (Arr, sll)

def distribute(Arr,d, sll):
    reminder = [0] * (len(Arr))

    for i in range(0,len(Arr)):
        # to get digits in the position we want we use
        r= (Arr[i]/ 10**d) % 10
        reminder[i] = r
    # print reminder

    # now distribute these values in single linked list

    for n in range(9,-1,-1):
        for m in range (len(Arr)-1,-1,-1):
            if sll.size == 0 and reminder[m] == n:
                sll.append(Arr[m])
                Arr.pop(m)
                reminder.pop(m)
            elif sll.size > 0 and reminder[m] == n:
                new_node = sllistnode(Arr[m])
                sll.appendleft(new_node)
                Arr.pop(m)
                reminder.pop(m)
                # print sll
            m -= 1
    return sll

def collect(Arr, ll):
    for i in range (ll.size):
       temp = ll.popleft()
       Arr.append(temp)
    # print Arr
    return Arr

rSort= [170, 45, 75, 90, 802, 24, 2, 66]
print 'Unsorted:', rSort
radixSort(rSort)
print rSort