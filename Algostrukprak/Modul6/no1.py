class MhsTIF:
    def __init__(self, nama, nim, tinggal, uangSaku):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.uangSaku = uangSaku
    def __str__(self):
        return(f"no1 nama = {self.nama}, nim = {self.nim}, tinggal = {self.tinggal} ")    


c0 = MhsTIF('Ika', 10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 230000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]


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
            if separuhKiri[i].nim < separuhKanan[j].nim: # while-lopp ini
                A[k]= separuhKiri[i] # menggabungkan kedua list, yakni
                i = i + 1 # separuhKiri dan separuhKanan,
            else: # sampai salah satu kosong.
                A[k] = separuhKanan[j]# Perhatikan kesamaan strukturnya
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
    for i in A:
        print(i)


# Recursive function to partition and sort the array
def quickSortBantu(A, low, high):
    if low < high:
        pivot = partition(A, low, high)  # Partition the array and get the pivot index
        quickSortBantu(A, low, pivot - 1)  # Recursively sort the left subarray
        quickSortBantu(A, pivot + 1, high)  # Recursively sort the right subarray

# Function to partition the array around the pivot
def partition(A, low, high):
    pivot = A[low].nim  # Select the pivot as the first element
    i = low + 1  # Initialize left index
    j = high  # Initialize right index

    while i <= j:
        while A[i].nim < pivot:  # Move left index until it finds a value greater than pivot
            i += 1

        while A[j].nim > pivot:  # Move right index until it finds a value less than pivot
            j -= 1

        if i <= j:  # Swap elements if left index is less than or equal to right index
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    return j  # Return the right index (pivot position) 

ls = [31, 20, 17, 44, 54, 77, 55, 93]
print("ini Merge Sort")
mergeSort(Daftar)
for i in mergeSort(Daftar):
    print(i)

print("\n\n ini quick sort")
quickSort(Daftar)