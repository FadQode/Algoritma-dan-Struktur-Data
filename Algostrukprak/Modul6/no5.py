import random
import sys



def mergeRecursive(A, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeRecursive(A, start, mid)
        mergeRecursive(A, mid + 1, end)
        merge(A, start, mid, end)
        
def merge(A, start, mid, end):
  i = start
  j = mid + 1
  k = start
  temp = [None] * (end - start + 1) 

  while i <= mid and j <= end:
    if A[i] < A[j]:
      temp[k - start] = A[i]
      i += 1
    else:
      temp[k - start] = A[j]
      j += 1
    k += 1

  while i <= mid:
    temp[k - start] = A[i]
    i += 1
    k += 1

  while j <= end:
    temp[k - start] = A[j]
    j += 1
    k += 1
  for i in range(start, end + 1):
    A[i] = temp[i - start]




def modMergeSort(A):
    mergeRecursive(A, 0, len(A) - 1)
    return A

random_list = [random.randint(1, 100) for _ in range(10)]


sys.setrecursionlimit(1000000000)
print(random_list)
print(modMergeSort(random_list))
print("Fadhil Erdya Q, 234")