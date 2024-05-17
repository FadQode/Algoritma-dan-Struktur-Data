from human import Manusia
class Mahasiswa(Manusia):
    """Class mahasiswa dengan berbagai metode"""
    def __init__(self, Nama, NIM,kota,us):
        """Constructor class Mahasiswa memberikan nilai  nilai pada properti object"""
        self.nama = Nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []

    def __str__(self):
        """dari Class Mahasiswa Mengeset nilai yang akan ditampilkan ketika object di print"""
        s = self.nama + ', NIM ' + str(self.NIM) \
        + '. Tinggal di ' + self.kotaTinggal \
        + '. Uang saku Rp ' + str(self.uangSaku) \
        + ' tiap bulannya.'
        return s
    
    def ambilNama(self):
        """Dari Class Mahasisswa Menampilkan Nama Object Mahasiswa"""
        return self.nama
    
    def ambilNIM(self):
        """Dari Class Mahasiswa Menampikan properti nim dari object ya"""
        return self.NIM
    
    def ambilUangSaku(self):
        """Dari Class Mahasiswa Menampilkan jumlah uang saku yang dimiliki mahasiswa """
        return self.uangSaku
    
    def ambilTempatTinggal(self):
        """Dari Class Mahasiswa Menampilkan rumah dari object Mahasiswa"""
        return self.kotaTinggal
    
    def perbaruiTempatTinggal(self, alamat):
        """Dari Class Mahasiswa Memperbarui Tempat Tinggal object Mahasiswa"""
        self.kotaTinggal = alamat
        return self.kotaTinggal
    
    def tambahUangSaku(self, uang):
        """Dari Class Mahasiswa Menambah uang saku Objek Mahasiswa"""
        self.uangSaku += int(uang)
        return self.uangSaku
    
    def raw_input(self, nama, NIM, kota, us):
        """Dari Class Mahasiswa Menginput data mahasiswa baru"""
        mhsLi = []
        mhs = Mahasiswa(nama, NIM, kota, us)
        mhsLi.append(str(mhs))
        return mhsLi
        

    def ambilMatkul(self, nama_matkul):
        """Dari Class Mahasiswa Menambah Matkul"""
        if nama_matkul in self.listKuliah:
            return "Matkul sudah diambil"
        else:
            self.listKuliah.append(nama_matkul)
            return self.listKuliah
            
    def removeMatkul(self, nama_matkul):
        if nama_matkul in self.listKuliah:
            self.listKuliah.remove(nama_matkul)
            return self.listKuliah
        else:
            return "Matkul tidak terdaftar"    


class MhsTIF(Mahasiswa): # perhatikan class induknya: Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        """Dari Class mhsTIF Memeberi Tahu bahwa python itu keren"""
        print('Python is cool.')        



mhs1 = MhsTIF("rizky", "L201", "Blora", 100000000)
m

        