import re

string = 'sebuah contoh batagor\!!'
cocok = re.search(r'kata:\w\w\w', string)
# Pernyataan-IF sesudah search() akan memeriksa apakah pencarian berhasil:
if cocok:
    print('menemukan'), cocok.group() ## ’menemukan kata:teh’
else:
    print('tidak menemukan')