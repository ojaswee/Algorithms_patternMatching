'''
In Radix Sorting is only used to sort numbers
First sort the number by unit digit then tens then hundreds and so on
This soring uses Linked List

'''
# import sys

def radixSort(Arr):
    #find max value in the array
    maxVal = max(Arr)
    digits = len(str(maxVal))  # find total digits in the max value
    radix(Arr, digits)

def radix(Arr,position):
    current= []
    for j in range(1,position):
        for i in range(len(Arr)):
            # currentD= int(str(Arr[i]))
            d= 10**j
            current= Arr[i]% d
            print Arr[i], current
        print '----', j,d

rSort= [12 ,13, 42, 103, 89, 8, 11]
radixSort(rSort)
# print 88% 10