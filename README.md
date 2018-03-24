# Sorting a list using differnt methods

In this excersice I wanted to sort a list or an array using differnt techniques
1) Bubble is basic sorting algorithm which sorts by conparing two consecutive elements in an array
    Space complexity: O(1)
    Time Complexity: O(n^2)    Best: O(n)
    
2) Selection sort first finds min value
    then we look in the array if we find another value less then
    current min we swap these values
    Space complexity: O(1)
    Time Complexity: O(n^2)    Best: O(n^2)
    
3) Insertion sort is better then then bubble and selection sort
    Insertion sort looks at an element
    if we have only one element it is always sorted so we start with
    comparing 2 values first select first element
    compare if this element is greater then values in the array
    if it is smaller then a value insert at right position
    Space complexity: O(1)
    Time Complexity: O(n^2)    Best: O(n)
    
4) Bucket sort as we put elements in bucket we need to sort it as well
    so first get an element then insert in the appropriate place in the bucket
    n = # elements, K = # buckets
    Space complexity: O(n)
    Time Complexity: O(n^2)    Worst: O(n^2)
    
5) Quick sort is very effective sorting technique
    most of the programs use this type of sorting when we call the sort function
    We do all the sorting in same array and we DONOT create another array
    Space complexity: O(log(n))
    Time Complexity: O(n log(n))    Worst: O(n^2)
    
6) Merge sort we first divide the array into individual elements
    compare this individual items and store them in new arrays
    Space complexity: O(n)
    Time Complexity: O(n log(n))   
    
7) In Radix Sorting is only used to sort numbers
    First sort the number by unit digit then tens then hundreds and so on
    This soring uses single Linked List
    n = #of elements , K = number of digits
    Space complexity: O(n+K)
    Time Complexity: O(nK)
    
8) Heap sort is useful when we are concerned about the memory usage during sorting
    Quick and merge sort use recursive method so they use more space then heap sort
    To do ascending heap sort we have to first create a max heapify.
    Max heapify has two children similar to complete binary search. First level
    has largest element, then second level has smaller elements then level and so on
    for example:  Max heapify of  {2,8,5,3,9,1} will be
            9
         /    \
        8      5
      /  \    /
    3     2  1
    We only heapify first part of array because right half is only going to have children
      1) After this we replace 1 with 9.
      2) detach 9 and continue with remaining elements
      3) now re-create max heapify from this tree
    Number of nodes each layer has is 2^(n-1)
    Space complexity: O(1)
    Time Complexity: O(n log(n))
    
9) Shell sort is modification to insertion sort
    we just compare 2 elements in a gap then rearrange them
    Time complexity = O(n(log(n))^2)
    Space Complexity = O (1)
