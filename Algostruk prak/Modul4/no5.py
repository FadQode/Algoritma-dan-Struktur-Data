#no6
def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1

    # Secara berulang belah runtutan itu menjadi separuhnya
    # sampai targetnya ditemukan
    while low <= high:
    # Temukan pertengahan runtut itu
        mid = (high + low) // 2
    # Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            return mid
    # ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
    # ataukah targetnya di sebelah kanannya?
        else:
            low = mid + 1
    # Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False

#no7
def binSe7(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1
    ansArr = []

    # Secara berulang belah runtutan itu menjadi separuhnya
    # sampai targetnya ditemukan
    while low <= high:
    # Temukan pertengahan runtut itu
        mid = (high + low) // 2
    # Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            ansArr.append(mid)
            while  mid - 1 > 0 and kumpulan[mid - 1] == target :
                if mid - 1 in ansArr:
                    mid -= 1
                    continue
                elif mid -1 is None:
                    break
                else:
                    ansArr.append(mid - 1) 
                    mid -= 1
            while mid + 1 < len(kumpulan) and kumpulan[mid + 1] == target:
                if mid + 1 in ansArr:
                    mid += 1
                    continue
                else:
                    ansArr.append(mid + 1)  
                    mid += 1
                      
            return ansArr        
    # ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
    # ataukah targetnya di sebelah kanannya?
        else:
            low = mid + 1
    # Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False

arr = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 11, 11, 11, 11]
print(binSe7(arr, 6))
print(binSe(arr, 6))

