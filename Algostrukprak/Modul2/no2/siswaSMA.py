from human import Manusia
class siswaSMA(Manusia):
    def __init__(self, nama, sekolah):
        self.nama = nama
        self.sekolah = sekolah
        print(self.sekolah)

    def pindahSekolah(self,sekolah):
        self.sekolah = sekolah
        return sekolah


