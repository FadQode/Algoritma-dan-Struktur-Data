#iterattive
def BinarySearch(numbers, val):
    first = 0
    last = len(numbers)-1
    index = -1
    print(numbers[15])
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

def ExponentialSearch(numbers, val):
    if numbers[0] == val:
        return 0
    index = 1
    while index < len(numbers) and numbers[index] <= val:
        index = index * 2
    print(numbers[:min(index, len(numbers))])    
    return BinarySearch( numbers[:min(index, len(numbers))], val)

numbers = [2,3,5,7,8,9,13,15,17,18,20,21,23,25,26,29,32,35,36]
index = ExponentialSearch(numbers, 25)
print(index)