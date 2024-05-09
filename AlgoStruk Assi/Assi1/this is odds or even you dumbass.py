#TODO 1



input1 = 0

while input1 != "quit":
    
    #Menerima Input dari user
    input1 = input("Masukkan Angka yang anda ingin cek: ")

    if input1 == "quit":
        break
    else:
        try :
            #mengubah input menjadi integer
            intput = int(input1)
        except:
            print("Angka yang anda Masukkan antara Bukan angka, atau bukan bilangan bulat")
        else:
            #Mengecek apakah angka prima atau bukan
            if intput % 2 == 0:
                #output ketika angka yang diberikan adalah prima
                print("Angka yang anda masukkan adalah prima")
            elif intput % 2 == 1:
                #output ketika angka yang diberikan adalah bukan prima
                print("Angka yang anda masukkan bukan prima") 
            else:
                print("Angka yang anda masukkan adalah 0")