from math import sqrt as sq

#deklarasi kelas
class distance():
    """Berisi kelas yang dapat digunakan untuk menetapkan dan mengukur jarak antar dua titik"""
    #deklarasi variabel titik 0, nilai awal variabel ini nanti akan digunakan sebagai titik awal(origin point)
    x = 0
    y = 0
    #deklarasi method untuk menetapkan titik baru
    def set_location(self, x, y):
        """Ubah koordinat anda"""
        #Cek tipe data input
        if not isinstance(x, int) or not isinstance(y, int):
            return "Tolong hanya masukkan angka integer"
        #self merujuk pada property yang dimiliki class
        self.x = x
        self.y = y
    #deklarasi method untuk  menghitung jarak titik dengan jarak asal (0,0)
    def distance_from_origin(self):
        "Cari tahu jarak titik anda dengan titik asal (0, 0)"
        #jarak ke titik (0, 0) dihitung menggunakan pythagoras
        return sq((self.x**2)+(self.y**2))

    #menerima argumen berupa titik kordinat yang akan dicari tahu jaraknya dari titik saat ini
    def distance_two_point(self, x2, y2):
        """menerima argumen berupa integer, masukkan x dan y yang anda ingin ketahui jaraknya dari titik saat ini"""
        #Cek tipe data input
        if not isinstance(x2, int) or not isinstance(y2, int):
            return "Tolong hanya masukkan angka integer"
        return sq((self.x-x2)**2+(self.y-y2)**2)


#buat Objek
jarak = distance()
#Test 1 Ubah titik dengan method set_location
print(f"titik x sebelum set location = {jarak.x}")
print(f"titik y sebelum set location = {jarak.y}")
print(f"jarak sebelum set location = {jarak.distance_from_origin()}")
jarak.set_location(21, 6)
print(f"titik x sesudah set location = {jarak.x}")
print(f"titik y sesudah set location = {jarak.y}")
#Test 2 hitung jarak titik baru dengan titik (0,0) dengan method distance_from_origin
print(f"jarak sesudah set location = {jarak.distance_from_origin()}")
#Test 3 menghitung jarak antar titik koordinat dengan method distance_two_point
print(f"Test 3 = {jarak.distance_two_point(10,12)}")
#Test 4 test input bukan angka
print(f"Test 4 = {jarak.set_location(1.2,2.3)}")
print(f"Test 4 = {jarak.distance_two_point("bukan", "angka")}")

print("Fadhil Erdya Qashmal (L200220234)")