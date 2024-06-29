def faktorPrima(angka: int) -> int:
    hasil = [1]
    bagiLagi = True
    while bagiLagi:
        bagiLagi = False
        for i in range(2, int(angka + 1)):
            if angka % i == 0:
                angka = angka / i
                print(i, angka)
                hasil.append(i)
                bagiLagi = True
                break
            else:
                continue
    return hasil    
print(faktorPrima(120))
            