#iterattive
def BinarySearch(numbers, val):
    first = 0
    last = len(numbers)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if numbers[mid] == val:
            index = mid
        else:
            if val < numbers[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


#recursive
# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

numbers = [2,3,5,7,8,9,13,15,17,18,20,21,23,25,26,29,32,35,36]
index = BinarySearch(numbers, 26)
print(index)