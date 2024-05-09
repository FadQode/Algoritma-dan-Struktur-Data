def longestWord(kata: str)-> str:
    """diberikan suatu string berisi kalimat Mengembalikan kata terpanjang pada kalimat tersebut"""
    #memisahkan tiap kata pada kalimat input
    splitted = kata.split(" ")
    #flag yang akan menampung jumlah huruf tiap kata dalam kalimat tersebut
    flag = 0
    #word yang akan menampung kata terpanjang dalam kalimat
    word = ""
    #perulangan dilakukan dari 0 hingga jumlah kata pada kalimat
    for i in range(0, len(splitted)):
        #jika jumlah huruf pada kata tersebut melebihi nilai flag 
        if len(splitted[i]) > flag:
            #maka panjang kata tersebut akan menjadi flag baru dan word akan menyimpan kata tersebut
            word = splitted[i]
            flag = len(splitted[i])
    #mengembalikan isi dari word
            
    print("L200220234 Fadhil Erdya Qashmal")        
    return f"Kata terpanjang adalah: {word}" 


kalimat = input("Masukkan suatu Kalimat ")  
print(longestWord(kalimat))

        

