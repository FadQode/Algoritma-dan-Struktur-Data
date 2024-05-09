"""Sistem Manajemen Bank minimal"""
class nasabah:
    """class nasabah yang akan mengatur segala kebutuhan nasabah yang memiliki akun dan rekening di bang ini
    """

    def __init__(self,  no_rekening, nama, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo
        

    
    def transfer(self, penerima, jumlah):
        try:
            if self.saldo - jumlah > 0:
                penerima.saldo = penerima.saldo + jumlah
                self.saldo = self.saldo - jumlah
                return f"transfer berhasil saldo {self.nama} tersisa {self.saldo}"
            else:
                return "saldo kurang" 
        except:
            return "user tidak ditemukan"

march = nasabah(1, "mitsuki",300000000 )
stelle = nasabah(2, "stelle", 1200000)

print(stelle.saldo)
print(march.transfer(stelle, 20000))
print(stelle.saldo)

"""Perbedaan List dan Tuple
1. List diinisialisasi menggunakan kurung siku [] sedang tuple dengan kurung biasa ()
2. isi list dapat ditambah dikurangi atau diubah, isi tuple tidak dapat diubah ubah
3. list lebih rentan terjadi error karena isinya yang dapat diubah ubah
4. performa dan ukuran tuple lebih stabi; karena ukurannya tetap"""


        