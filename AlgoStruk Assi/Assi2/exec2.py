class kendaraan():
    """Class yang berisi berbagai properti yang dimiliki oleh kendaraan"""

    def __init__(self, name, color, year_production, capacity, mileage):
        """Constructor yang digunakan untuk menetapkan berbagai properti yang dimiliki oleh kendaraan
          ketika suatu objek kendaraan dibuat """
        self.name = name
        self.color = color
        self.year_production = year_production
        self.capacity = capacity
        self.mileage = mileage
        #penanda kalau objek berhasil dibuat maka akan menampilkan teks dibawah
        print("Objek dari kelas kendaraan atau anak anaknya telah berhasil dibuat")

    def set_capacity(self, capacity: int):
        """Method set capacity yang digunakan untuk mengatur jumlah kapasitas 
        yang dimiliki objek kendaraan"""
        self.capacity = capacity

class truck(kendaraan):
    """class truck adalah child class dari class kendaraan kelas ini memiliki 
    semua properti kelas kendaraan dan dapat menggunakan semua method dan constructor nya ,
    serta mempunyai properti baru, size yang sudah memiliki nilai yang  "big" yang menggambarkan suatu truk"""
    size = "big"

#Test 1 membuat objek dari class truk dengan memasukkan parameter constructor yang dimiliki kelas kendaraan
truk =  truck("Hino", "green", 2021, 5, 20001)
truknt =  kendaraan("volvo", "red", 2022, 2, 20222)

#Test 2 Menggunakan properti dan method class kendaraan pada objek dari class truck 
print(f"kapasitas truk sebelum digunakan method = {truk.capacity}")  
truk.set_capacity(2)
print(f"kapasitas truk setelah digunakan method = {truk.capacity}")
print(f"Nama Merk Truk = {truk.name}")
print(f"Total jarak yang sudah ditempuh = {truk.mileage}")
print(f"Tahun Pembuatan truk = {truk.year_production}")
#Test 3 Memanggil properti yang terdapat pada class truck itu sendiri
print(f"Ukuran truk = {truk.size}")
try:
    print(f"Ukuran truknt = {truknt.size}")
except:
    print("class kendaraan tidak punya attribut size")

print("Fadhil Erdya Qashmal (L200220234)")