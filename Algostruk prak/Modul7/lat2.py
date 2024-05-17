import re

# Mencari pola 'eee' pada string 'teeeh'
cocok = re.search(r"eee", "teeeh")  # Temukan, cocok.group() == "eee"
if cocok:
    print(f"Pola 'eee' ditemukan: {cocok.group()}")
else:
    print("Pola 'eee' tidak ditemukan")

# Mencari pola 'ehs' pada string 'teeeh'
cocok = re.search(r"ehs", "teeeh")  # Tidak ditemukan, cocok == None
if cocok:
    print(f"Pola 'ehs' ditemukan: {cocok.group()}")
else:
    print("Pola 'ehs' tidak ditemukan")

# Mencari pola '..h' pada string 'teeeh'
cocok = re.search(r"..h", "teeeh")  # Temukan, cocok.group() == "eeh"
if cocok:
    print(f"Pola '..h' ditemukan: {cocok.group()}")
else:
    print("Pola '..h' tidak ditemukan")

# Mencari pola '\d\d\d' pada string 't123h'
cocok = re.search(r"\d\d\d", "t123h")  # Temukan, cocok.group() == "123"
if cocok:
    print(f"Pola '\\d\\d\\d' ditemukan: {cocok.group()}")
else:
    print("Pola '\\d\\d\\d' tidak ditemukan")

# Mencari pola '\w\w\w' pada string '@@abcd!!'
cocok = re.search(r"\w\w\w", "@@abcd!!")  # Temukan, cocok.group() == "abc"
if cocok:
    print(f"Pola '\\w\\w\\w' ditemukan: {cocok.group()}")
else:
    print("Pola '\\w\\w\\w' tidak ditemukan")
