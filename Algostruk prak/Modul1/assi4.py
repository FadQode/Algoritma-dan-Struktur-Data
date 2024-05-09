def rerata(b: list) -> list:
    hasil = 0
    jumlah = 0
    for i in range(len(b)):
        jumlah += b[i]

    hasil = jumlah / len(b)
    return hasil

print(rerata([1,2,3,4,5]))