def katakan(n):

    if n == 100:
        return "seratus"
    elif n == 1000:
        return "seribu"
    elif n == 1000000:
        return "sejuta"        
    if n == 0:
        return "nol"
    elif n < 10:
        return ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"][n - 1]
    elif n < 20:
        return ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"][n - 10]
    elif n < 100:
        return f"{['', 'sepuluh', 'dua puluh', 'tiga puluh', 'empat puluh', 'lima puluh', 'enam puluh', 'tujuh puluh', 'delapan puluh', 'sembilan puluh'][n // 10]} {katakan(n % 10)}"
    elif n < 1000:
        return f"{katakan(n // 100)} ratus {katakan(n % 100)}"
    elif n < 1000000:
        return f"{katakan(n // 1000)} ribu {katakan(n % 1000)}"
    elif n < 1000000000:
        return f"{katakan(n // 1000000)} juta {katakan(n % 1000000)}"

angka =  int(input("Masukkan angka yang anda ingin cek: "))
if angka > 1000000000:
    print("Angka yang anda masukkan lebih dari satu miliar")
else:
    print(katakan(angka))


print("Fadhil Erdya Qashmal L200220234")


