class MhsTIF:
    def __init__(self, nama, nim, tinggal, uangSaku):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.uangSaku = uangSaku
    def __str__(self):
        return(f"no1 nama = {self.nama}, nim = {self.nim}, tinggal = {self.tinggal} ")    

def cariLurus( wadah, target ):
    arr = []
    n = len( wadah )
    for i in range( n ):
        if wadah[i] == target:
            arr.append[i]
    return arr


c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 230000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
#no 1
target = 'Klaten'
jwbArr = []
for i in range(len(Daftar)):
    if Daftar[i].tinggal == target:
        jwbArr.append(Daftar[i])
for i in jwbArr:        
    print(i)        
       

#no2
def uangSakuTerkecil(arr):        
    terkecil = arr[0].uangSaku
    for i in Daftar:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
            nama = i.nama
            nim = i.nim
    return f"no2 {terkecil} milik {nama} yang punya nim {nim}" 

print(f"no2 uang saku terkecil adalah {uangSakuTerkecil(Daftar)}")
#no3
def uangSakuTerkecilBanyak(arr):
    terkecil = arr[0].uangSaku
    listarr = []
    for i in arr:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    for i in arr:
        if i.uangSaku == terkecil:
            listarr.append(i)
    for i in range(len(listarr)):
        print(f"{listarr[i].uangSaku} milik {listarr[i].nama} yang punya nim {listarr[i].nim}\n")
    return

# print(f"uang saku terkecil adalah {uangSakuTerkecilBanyak(Daftar)}")
print("no3")
uangSakuTerkecilBanyak(Daftar)

#no4
def uangSaku250k(arr):
    listarr = []
    for i in arr:
        if i.uangSaku < 250000:
            listarr.append(i)
    print("Orang yang memiliki uang saku dibawah 250k")        
    for i in listarr:
        print(f"no 4 nama: {i.nama}\n nim: {i.nim} \n uang saku: {i.uangSaku}")      

uangSaku250k(Daftar)