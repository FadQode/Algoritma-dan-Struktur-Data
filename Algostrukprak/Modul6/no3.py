from time import time as detak
from random import shuffle as kocok
import sys


k = list(range(1 , 6001))
kocok(k)

u_bub = k[:]  # Copy list k to u_bub
u_sel = k[:]  # Copy list k to u_sel
u_ins = k[:]  # Copy list k to u_ins (don't forget the [:])
u_mrg = k[:]  # Copy list k to u_mrg
u_qck = k[:]  # Copy list k to u_qck
u_mmrg = k[:]
U_qck3 = k[:]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):

        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return arr
        
def insertionSort(arr):
	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            
            if array[i] < array[min_idx]:
                min_idx = i
         
        
        (array[step], array[min_idx]) = (array[min_idx], array[step])
def mergeSort(A):
    #print "Membelah ", A
    if len(A) > 1:
        mid = len(A) // 2 # Membelah list.
        separuhKiri = A[:mid] # Slicing ini langkah yang expensive sebenarnya,
        separuhKanan = A[mid:] # bisakah kamu membuatnya lebih baik?

        mergeSort(separuhKiri) # Ini rekursi. Memanggil lebih lanjut mergeSort
        mergeSort(separuhKanan) # untuk separuhKiri dan separuhKanan.
    # Di bawah ini adalah proses penggabungan.
        i=0 ; j=0 ; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]: # while-lopp ini
                A[k] = separuhKiri[i] # menggabungkan kedua list, yakni
                i = i + 1 # separuhKiri dan separuhKanan,
            else: # sampai salah satu kosong.
                A[k] = separuhKanan[j] # Perhatikan kesamaan strukturnya
                j = j + 1 # dengan proses penggabungan
            k=k+1 # dua list urut.

        while i < len(separuhKiri): # Jika separuhKiri mempunyai sisa
            A[k] = separuhKiri[i] # tumpukkan ke A
            i = i + 1 # satu demi satu.
            k = k + 1 #

        while j < len(separuhKanan): # Jika separuhKanan mempunyai sisa
            A[k] = separuhKanan[j] # tumpukkan ke A
            j = j + 1 # satu demi satu.
            k = k + 1
    return A

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)  # Call quickSortBantu recursively

# Recursive function to partition and sort the array
def quickSortBantu(A, low, high):
    if low < high:
        pivot = partition(A, low, high)  # Partition the array and get the pivot index
        quickSortBantu(A, low, pivot - 1)  # Recursively sort the left subarray
        quickSortBantu(A, pivot + 1, high)  # Recursively sort the right subarray

# Function to partition the array around the pivot
def partition(A, low, high):
    pivot = A[low]  # Select the pivot as the first element
    i = low + 1  # Initialize left index
    j = high  # Initialize right index

    while i <= j:
        while A[i] < pivot:  # Move left index until it finds a value greater than pivot
            i += 1

        while A[j] > pivot:  # Move right index until it finds a value less than pivot
            j -= 1

        if i <= j:  # Swap elements if left index is less than or equal to right index
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    return j 

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

def partition3(A, left, right):
  pivot = median_of_three(A, left, right)
  i = left - 1

  for j in range(left, right):
    if A[j] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]

  A[i + 1], A[right] = A[right], A[i + 1]
  return i + 1

def quickSort3(A, left, right):
  if left < right:
    pivot_index = partition3(A, left, right)
    quickSort3(A, left, pivot_index - 1)
    quickSort3(A, pivot_index + 1, right)


# Mengukur waktu untuk setiap algoritma pengurutan
aw = detak()  # Catat waktu awal
bubbleSort(u_bub)
ak = detak()  # Catat waktu akhir
print('Bubble Sort: %g detik' % (ak - aw))

aw = detak()
selectionSort(u_sel, len(u_sel))
ak = detak()
print('Selection Sort: %g detik' % (ak - aw))

aw = detak()
insertionSort(u_ins)
ak = detak()
print('Insertion Sort: %g detik' % (ak - aw))

aw = detak()
mergeSort(u_mrg)
ak = detak()
print('Merge Sort: %g detik' % (ak - aw))

sys.setrecursionlimit(10000)
aw = detak()
quickSort(u_qck)
ak = detak()
print('Quick Sort: %g detik' % (ak - aw))

aw = detak()
modMergeSort(u_mmrg)
ak = detak()
print('Modified Merge Sort: %g detik' % (ak - aw))

aw = detak()
quickSort3(U_qck3, 0, len(U_qck3) -1)
ak = detak()
print('Modified Quick Sort: %g detik' % (ak - aw))

print("Fadhil E 234")