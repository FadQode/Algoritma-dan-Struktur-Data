from random import randint

def game():
    life = 10
    correct = randint(1,101)
    jawaban = int(input("Telah dipilih satu angka dari 1 hingga 100 coba tebak dalam tebakan: "))
    while life > 1:   
        if jawaban < correct:
            life -= 1
            print(f"angka yang kamu tebak terlalu kecil coba lagi, {life} kesempatan tersisa")
            jawaban = int(input("Tebak Lagi: "))
        elif jawaban > correct:
            life -= 1
            print(f"angka yang kamu tebak terlalu besar coba lagi, {life} kesempatan tersisa")   
            jawaban = int(input("Tebak Lagi: "))
        elif jawaban == correct:
            print("Jawaban yang kamu tebak benar Selamat")
            return
    if life == 1:    
      print(f"Yah kamu gagal, jawaban yang benar adalah {correct} silakan coba lagi ya")
      return

game()   
        





