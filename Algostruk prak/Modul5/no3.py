from time import time as detak
from random import shuffle as kocok

k = list(range(1 , 60001))
kocok(k)
u_bub = k[:] ## \\
u_sel = k[:] ## -- Jangan lupa simbol [:]-nya!.
u_ins = k[:] ## //
built_in = k[:]

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



aw=detak();selectionSort(u_sel, len(u_sel));ak=detak();print('selection: %g detik' %(ak-aw) );
aw=detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' % (ak-aw) );
aw=detak();sorted(built_in);ak=detak();print('built in sort: %g detik' % (ak-aw) );
aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw) );
