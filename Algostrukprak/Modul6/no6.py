import random
import sys

def median_of_three(A, left, right):
  mid = left + (right - left) // 2
  if A[left] > A[mid]:
    A[left], A[mid] = A[mid], A[left]
  if A[left] > A[right]:
    A[left], A[right] = A[right], A[left]
  if A[mid] > A[right]:
    A[mid], A[right] = A[right], A[mid]


  pivot = A[mid]
  A[mid], A[right] = A[right], A[mid]  
  return pivot

def partition(A, left, right):
  pivot = median_of_three(A, left, right)
  i = left - 1
  for j in range(left, right):
    if A[j] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]


  A[i + 1], A[right] = A[right], A[i + 1]
  return i + 1

def quickSort(A, left, right):
  if left < right:
    ans= partition(A, left, right)
    quickSort(A, left, ans- 1)
    quickSort(A, ans+ 1, right)

# Example usage
A = [random.randint(1, 100) for i in range(10)]


sys.setrecursionlimit(1000000000)
print(A)
quickSort(A, 0, len(A) - 1)
print(A) 
print("L200220234, Fad Qash")