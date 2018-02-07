'''Bucket sort is similar to radix sort, the only difference is
1) we distribute only once
2) we need to create a container and
3)within container we need to sort all the elemets
'''


def sort_bucket(A,left, right):
    size = right-left+1
    j = 0
    for i in range(0, size):
        temp = A[i]
        for j in range(i-1,-2,-1):
            if (temp<A[j]):
                A[j+1]=A[j]
            else: break
        A[j+1] = temp
    # print 'Insertion Sort:',A

def bucketSort(Arr, n=5):
    maxVal = max (Arr)
    minVal = min(Arr)
    bucket = 5
    count = (maxVal-minVal)/bucket
    count_elements = [0] * bucket    # counting number of elements in an bucket
    temp_Arr = []

    #put values in priority queue/dictionary
    for i in range(len(Arr)):
        if (Arr[i]<count):
            temp_Arr.append((0,Arr[i]))
            count_elements[0] +=1
        elif Arr[i] in range (count, 2*count):
            temp_Arr.append ((1, Arr[i]))
            count_elements[1] += 1
        elif Arr[i] in range (2*count, 3*count):
            temp_Arr.append ((2, Arr[i]))
            count_elements[2] += 1
        elif Arr[i] in range(3 * count, 4 * count):
            temp_Arr.append ((3, Arr[i]))
            count_elements[3] += 1
        else:
            temp_Arr.append ((4, Arr[i]))
            count_elements[4] += 1

    temp_Arr= sorted(temp_Arr, key=lambda x: (x[0]))
    Arr = [i[1] for i in temp_Arr]
    print count_elements, Arr

    # for i in range (len(Arr)):
    start = 0
    for j in range(bucket):
        if j == 0 and count_elements[j]>0:
            sort_bucket(Arr, 0, count_elements[j])
            print 0,count_elements[j]-1
        elif j >0 and count_elements[j]>1:
            end = start + count_elements[j] -1
            print start, end
            sort_bucket(Arr,start, end)
        start += count_elements[j]
    return Arr

'''801 not printing in correct order'''
bSort= [800,170, 45, 90, 24, 2,855, 900, 605, 66, 801]
print 'Unsorted:', bSort
bSort= bucketSort(bSort)
print bSort