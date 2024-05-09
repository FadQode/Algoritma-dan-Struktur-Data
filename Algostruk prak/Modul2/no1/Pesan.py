class Pesan(object):
    """
    Sebuah class bernama Pesan.
    Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString

    def cetakIni(self):
        print(self.teks)

    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))

    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))

    def jumKar(self):
        return len(self.teks)
    
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')

    def perbarui(self,stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, masukan):
        if masukan in self.teks:
            return True
        else: return False

    def hitungKonsonan(self):
        hurufVokal = ["a", "i", "u", "e", "o", "A", "I", "E", "O", "U"]
        flag = 0
        for i in range(len(self.teks)):
            if  self.teks[i] not in hurufVokal:
                flag += 1
            else:
                continue
                
        return flag   
    
    def hitungVokal(self):
        hurufVokal = ["a", "i", "u", "e", "o"]
        flag = 0
        for i in range(len(self.teks)):
            if  self.teks[i] in hurufVokal:
                flag += 1 
            else:
                continue
        return flag             