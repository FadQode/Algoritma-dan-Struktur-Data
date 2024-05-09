"""Program ini berisi fungsi yang jika dijalankan dengan diisi suatu parameter berupa integer maka akan
menjumlahkan seluruh angka dari satu hingga angka yang menjadi parameter"""

#Deklarasi fungsi berparameter
def substract(angka: int)->int:
    #variabel result untuk menampung hasil
    result = 0
    
    #Memastikan Parameter yang masuk berupa Integer
    if not isinstance(angka, int):
        return "Parameter yang anda masukkan bukan integer"
    #mengecek apakah angka kurang dari 0    
    elif angka < 0:
        #jika angka kurang dari 0 maka parameter akan dikalikan -1 untuk mengubah menjadi positif
        b = angka * -1
        #lalu akan dilakukan looping hingga nilai parameter positif    
        for i in range(b + 1):
            #setiap variabel looping dikalikan -1
            a = i * -1
            #setelah dikali -1 lalu ditambahkan sehingga menghasilkan penjumlahan untuk angka negatif
            result += a
    #mengecek apakah angka lebih dari 0 
    elif angka > 0:
        #jika angka lebih dari 0 dilakukan pengulangan hingga angka parameter
        for i in range(angka + 1):
            #setiap angka pengulangan dijumlahkan dan disimpan 
            result += i
    #program yang dieksekusi jika parameter sama dengan 0         
    elif angka == 0:
        return "Parameter yang anda masukkan bernilai 0"
        
    #akhir dari fungsi, mengembalikan nilai hasil
    return result


#Test 1 Penjumlahan angka positif
print(f"Test 1: {substract(20)}") 
#Test 2 Penjumlahan angka positif 2
print(f"Test 2: {substract(5)}") 
#Test 3 Penjumlahan angka negatif
print(f"Test 3: {substract(-13)}")
#Test 4 Parameter yang diberikan bukan integer
print(f"Test 4: {substract("Percobaan")}")
#Test 5 Parameter bernilai 0
print(f"Test 5: {substract(0)}")

print("Fadhil Erdya Qashmal(L200220234)")
