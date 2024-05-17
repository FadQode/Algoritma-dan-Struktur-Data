import re

## Misal kita punya banyak alamat email
s = 'Alamatku sri@google.com serta joko@abc.com ok bro.'
## Di sini re.findall() mengembalikan sebuah list beranggotakan string alamat
emails = re.findall(r'[\w\.-]+@[\w\.-]+', s) ##=> ['sri@google.com', 'joko@abc.com']
for email in emails:
# lakukan sesuatu untuk tiap-tiap email yang ditemukan
    print(email)


f = open('test.txt', 'r') ## membuka file.
p = r'sebuah pola+' ## ini polanya.
## memberikan seluruhnya ke findall()
## dia mengembalikan list beranggotakan string yang cocok
strings = re.findall(p, f.read())  
for string in strings:
    print(string)

s = 'Alamatku agung@google.com, ag@t.co, atau bob@abc.com ok bro?'
pola = r'([\w\.-]+)@([\w\.-]+)'
tuples = re.findall(pola, s)
print(tuples)
##==> [('agung', 'google.com'), ('ag','t.co'), ('bob', 'abc.com')]
## Atau kita cetak satu per satu:
for tup in tuples:
    print(f"user {tup[0]} dengan host:{tup[1]}")