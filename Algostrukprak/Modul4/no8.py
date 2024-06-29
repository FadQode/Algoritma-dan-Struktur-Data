from random import randint
def game():
    a = []
    for i in range(0, 1001):
        a.append(i)
    return a

def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1
    iterasi = 0
    # Secara berulang belah runtutan itu menjadi separuhnya
    # sampai targetnya ditemukan
    while low <= high:
        iterasi += 1
        print(iterasi)
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

binSe(game(), 1000)
binSe(game(), 100)