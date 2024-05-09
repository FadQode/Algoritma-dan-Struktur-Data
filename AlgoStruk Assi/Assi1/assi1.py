"""Program ini akan mengecek apakah input parameter integer yang diterimanya suatu bilangan prima"""

#Deklarasi fungsi berparameter
def primeChecker(number: int) -> int:
    #mengecek apakah input parameter adalah suatu integer   
    if not isinstance(number, int):
         return "Pastikan anda Memasukkan int sebagai Parameter"
    #mengecek apakah input parameter bernilai 0 atau berupa bilangan negatif
    elif number <= 0:
         return "nol bukan bilangan prima ataupun komposit dan tidak ada bilangan prima negatif!"
    #setelah diapastikan merupakan interger tidak bernilai 0 atau negatif maka akan dicek apakah prima atau bukan
    else:
        #variabel berisi jawaban yang akan berubah tergantung dari input parameternya
        answer = True
        #Mengecek apakah bilangan prima atau bukan
        for x in range(2, number):
            if number % x == 0:
                answer = False
                break
        #jika variabel answer masih True maka bilangan prima    
        if answer:
            answer = "Adalah Prima"
        #jika answer Bernilai false maka bilangan tidak prima    
        else: 
            answer = "Bukanlah Prima"
        #Mengembalikan     
        return answer 

#Test 1 mengecek keprimaan angka 1 sampai 20
for i in range (21):
    print(f"Angka Input {i}: {primeChecker(i)}")        
#Test 2 Input bilangan negatif
print(f"Test 2: {primeChecker(-15)}") 
#Test 3 Input parameter bertipe data selain int
print(f"Test 3: {primeChecker(12.345)}") 

print("Fadhil Erdya Qashmal(L200220234)")
    
