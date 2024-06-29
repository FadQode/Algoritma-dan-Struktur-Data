import re

# Mencari pola 'e+' pada string 'teeeh'
cocok = re.search(r"e+", "teeeh")  # Temukan, cocok.group() == "teee"
if cocok:
    print(f"Pola 'e+' ditemukan: {cocok.group()}")
else:
    print("Pola 'e+' tidak ditemukan")

# Mencari pola 'e+' dengan solusi paling kiri (tidak mengambil kelompok 'ee' kedua)
cocok = re.search(r"e+", "teeheeee")  # Temukan, cocok.group() == "ee"
if cocok:
    print(f"Pola 'e+' ditemukan: {cocok.group()}")
else:
    print("Pola 'e+' tidak ditemukan")

# Mencari 3 angka yang dipisahkan spasi/tab (nol atau lebih)
cocok = re.search(r"\d\s*\d\s*\d", "xx1 2 3xx")  # Temukan, cocok.group() == "1 2 3"
if cocok:
    print(f"Pola '\\d\\s*\d\\s*\d' ditemukan: {cocok.group()}")
else:
    print("Pola '\\d\\s*\d\\s*\d' tidak ditemukan")

cocok = re.search(r"\d\s*\d\s*\d", "xx12 3xx")  # Temukan, cocok.group() == "12 3"
if cocok:
    print(f"Pola '\\d\\s*\d\\s*\d' ditemukan: {cocok.group()}")
else:
    print("Pola '\\d\\s*\d\\s*\d' tidak ditemukan")

cocok = re.search(r"\d\s*\d\s*\d", "xx123xx")  # Temukan, cocok.group() == "123"
if cocok:
    print(f"Pola '\\d\\s*\d\\s*\d' ditemukan: {cocok.group()}")
else:
    print("Pola '\\d\\s*\d\\s*\d' tidak ditemukan")

# Mencocokkan kata yang dimulai dengan 'k' di awal string
cocok = re.search(r"^k\w+", "mejakursi")  # Tidak ditemukan, cocok == None
print("Pola '^k\\w+' tidak ditemukan")

# Mencocokkan kata yang dimulai dengan 'k' di mana saja dalam string
cocok = re.search(r"k\w+", "mejakursi")  # Temukan, cocok.group() == "kursi"
print(f"Pola 'k\\w+' ditemukan: {cocok.group()}")

s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.search(r'\w+@\w+', s)
if cocok:
    print(f"pola '\w+@\w+' ditemukan:{cocok.group()}")## => ’b@google’
else:
    print(f"pola '\w+@\w+' tidak ditemukan")

cocok = re.search(r'[\w.-]+@[\w.-]+', s)
if cocok:
    print(f"pola '\w+@\w+' ditemukan:{cocok.group()}")## => ’b@google’
else:
    print(f"pola '\w+@\w+' tidak ditemukan")

pola = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', s) 
if cocok:
    print(f"pola '\w+@\w+' ditemukan:{cocok.group()}")## => ’b@google’
else:
    print(f"pola '\w+@\w+' tidak ditemukan")

