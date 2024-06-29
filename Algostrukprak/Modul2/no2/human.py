class Manusia():
    """ Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        """Dari class Manusia memberi salam"""
        print("Salaam, namaku", self.nama)
    def makan(self, s):
        """Dari class Human menampilkan sesuatu yang bari saja dimakan"""
        print("Saya baru saja makan", s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        """Dari class human menampilkan apa olahraga uang baru saja dilakukan"""
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        """Dari class manusia, manusia yang tidak bisa perkalian dua"""
        return n*2

