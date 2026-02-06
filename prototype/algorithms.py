# Selection Sort
#     Brute Force, Sorting Algorithm
#     Objective: Given an array of size k, sort it in
#     ascending/decending order by comparing every element
#     to every other element.
def selection_sort_min(arr):
    n = len(arr)
    # iterate through the array, saving the first index as the temp min
    for i in range(n-1):
        min_id = i
        # iterate through the rest of the array,
        # comparing each element with the current min_id
        for j in range(i+1, n):
            # change the min_id if necessary,
            # then swap the values in the actual array
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i], arr[min_id] = arr[min_id], arr[i]
def selection_sort_max(arr):
    n = len(arr)
    # iterate through the array, saving the last index as the temp max
    for i in range(n-1):
        max_id = i
        # iterate through the rest of the array,
        # comparing each element with the current max_id
        for j in range(i+1, n):
            # change the max_id if necessary,
            # then swap the values in the actual array
            if arr[j] > arr[max_id]:
                max_id = j
        arr[i], arr[max_id] = arr[max_id], arr[i]



# Insertion Sort
#     Incremental, Sorting Algorithm
#     Objective: Given an array of size k, sort it in
#     ascending/descending order by iterating through
#     the list, actively changing it when necessary.
def insertion_sort(arr):
    n = len(arr)
    # iterate through the array, starting from the second element
    for i in range(1, n):
        # save the current element as the key
        # to be compared with the previous elements
        key = arr[i]
        # compare the current element with the previous elements
        j = i-1
        # shift the elements greater than the key to the right
        # if necessary, then make
        while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key



# Merge Sort
#     Divide and Conquer, Sorting Algorithm
#     Objective: Given an array of size k, sort it in
#     ascending/decending order by...
#     1. choosing a pivot element to base everything off of
#     2. paritioning the array around the pivot element
#     3. recursively doing the same thing for the two different halves now

#necessary method to combine the sublists into one
def merge(arr, left, mid, right):
    # find the middle point to divide the array into two halves
    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    temp1 = [0] * n1
    temp2 = [0] * n2

    # copy data to temp arrays
    for i in range(n1):
        temp1[i] = arr[left + i]
    for j in range(n2):
        temp2[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # merge the temp arrays back into arr[left..right]
    # by comparing the same index of the two elements
    # and adding the correct one based on their values
    # before adding the other one
    # this happens constantly between lis
    while i < n1 and j < n2:
        if temp1[i] <= temp2[j]:
            arr[k] = temp1[i]
            i += 1
        else:
            arr[k] = temp2[j]
            j += 1
        k += 1

    # copy the remaining elements, if there are any
    while i < n1:
        arr[k] = temp1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = temp2[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    #the function is recursively solved
    #by divided the array in half until it only has one element,
    #which is then combined with its originally adjacent elements
    #through merge. through that combining process, it's sorted.
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)



# Quick Sort
#     Divide and Conquer, Sorting Algorithm
#     Objective: Given an array of size k, sort it in
#     sort it by...
#     1. dividing the array recursively into halves until it can't be anymore
#     2. sorting each subarray individually
#     3. combined the subarrays into a single array
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)



# Kadane's Algorithm
#     Dynamic Programming, Mathematical Algorithm
#     Objective: Given an array, find the subarray that
#     has the max sum and return it

def kadane(arr):
    # initialize 2 variables. res holds the max so far,
    # and maxEnd is the 'counter' that you compare res to
    res = arr[0]
    maxEnd = arr[0]
    for i in range(1, len(arr)):
        # if current element is greater than maxEnd,
        # then it becomes the new maxEnd,
        # else it adds itself to maxEnd
        maxEnd = max(maxEnd + arr[i], arr[i])
        res = max(res, maxEnd)
    return res




# Karatsuba's Algorithm
#     Divide and Conquer, Mathematical Algorithm
#
# Counting Sort
#     Brute Force, Sorting Algorithm
# Radix Sort
#     Divide and Conquer, Sorting Algorithm
# Bucket Sort
#     Incremental, Sorting Algorithm
#
# Heapsort
#     Incremental, Sorting Algorithm
#
