"""Program ini berisi Fungsi yang jika dijalankan dan di masukkan parameter berupa list yang berisi 
tipe data integer dengan nilai yang terduplikat di dalamnya maka akan mengembalikan output berupa 
list yang sama tanpa ada nilai duplikat didalamnya """

#Deklarasi Fungsi dengan Parameter yang menerima input list
def removeSameComp(listParam: list) -> list:
    #list kosong untuk menampung list tanpa adanya duplikat nilai
    cleanList = []
    #Mengecek apakah nilai list parameter berupa list kosong
    if listParam == cleanList:
        return "List yang dimasukkan kosong"
    #setelah pengecekan list kosong akan dicek apakah parameter berupa suatu list 
    elif isinstance(listParam, list):
            for i in range(len(listParam)):
            #memastikan nilai setiap unsur list parameter adalah integer(tes tipe data)
                if not isinstance(listParam[i], int):
                    return "Terdapat value yang bukan int pada list yang anda masukkan"
            #mengecek apakah unsur ke-i dalam list parameter sudah terdapat dalam cleanlist(tes duplikasi)
                elif listParam[i] in cleanList:
                    continue
            #jika nilai ke-i list parameter melewati tes tipe data dan tes duplikat maka nilai tersebut akan dimasukkan ke cleanlist
                else:
                    cleanList.append(listParam[i])
            #akhir dari fungsi mengembalikan list tanpa duplikat             
            return cleanList    
    
    #program yang dijalankan jika parameter bukan suatu list 
    else:
        return "Parameter yang anda Masukkan bukan merupakan suatu list"
    

#Test 1 List dengan nilai duplikat acak
print(f"Test 1: {removeSameComp([23, 24, 25, 26, 23, 23, 23, 23, 24, 25, 2, 5, 65])}")  
#Test 2 List dengan nilai duplikat berurutan
print(f"Test 2: {removeSameComp([2,2,3,4,4,4,5,5,6,7])}")  
#Test 3 tes list tanpa nilai duplikat
print(f"Test 3: {removeSameComp([2,10,11,12,13,14,15])}")  
#Test 4 input bukan list
print(f"Test 4: {removeSameComp("aaa")}")
#Test 5 input dengan unsur list bukan integer 
print(f"Test 5: {removeSameComp([2,10,"string",12.23,13,14,15])}") 
#Test 6 input list kosong
print(f"Test 6: {removeSameComp([])}") 

print("Fadhil Erdya Qashmal(L200220234)")
