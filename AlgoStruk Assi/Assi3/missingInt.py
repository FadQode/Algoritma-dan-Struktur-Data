# def missInt(sepuluh: list)-> list:
#     for i in range(1,len(sepuluh)+1):
#         print(i, sepuluh[i] - 1)
#         if i != sepuluh[i] - 1:
#             return f"Bilangan yang hilang adalah bilangan {i + 1}"
#     return"Bilangan Lengkap"

# print(missInt([1, 2, 3, 4, 5, 7, 8, 9, 10]))



def missInt(sepuluh: list)-> list:
    """Mengembalikan satu nilai yang hilang pada suatu list berisi angka 1 hingga 10"""
    #menyiapkan suatu list lengkap berisi angka 1 hingga 10
    complete = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #melakukan perulangan terhadap setiap nilai di list yang lengkap
    for i in range(0,len(complete)):
        #mencoba apakah terjadi error jika mengakses index ke i dari list input
            try:
                a = sepuluh[i]
            except:
            #Jika error maka akan mengembalikan angka yang hilang
                return f"Bilangan yang hilang adalah {complete[0]}" 
            else:
            #mengecek apakah indeks ke i dari list sepuluh terdapat dalam list lengkap    
                if a in complete:
                    #jika tidak terjadi error maka indeks ke i list input akan dihapus dari list yang lengkap
                    complete.remove(a)
                else:
            #jika indeks ke i list sepuluh tidak ada dalam list lengkap maka itu bukan bilangan satu sampai sepuluh         
                     return "Terdapat bilangan tak dikenal"
                         
    return "List lengkap dari 0 hingga 10"                
                         
#List berurutan dari 1 hingga 10 kehilangan satu angka       
print(f"Tes 1 = {missInt([1, 2, 3, 5, 6, 7, 8, 9, 10])}")
#List tidak berurutan dari 1 hingga 10 kehilangan satu angka  
print(f"Tes 2 = {missInt([2, 4, 6, 1, 8, 9, 3, 7, 5])}")
#List lengkap dari 1 hingga ke sepuluh
print(f"Tes 3 = {missInt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
#List terdapat nilai yang buka satu sampai sepuluh
print(f"Tes 4 = {missInt([1, 2, 3, 4, 23, 7, 8, 9, 10])}")
print("Fadhil Erdya Qashmal L200220234")