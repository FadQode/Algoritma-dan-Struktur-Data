from no1 import Stack

PROMPT = "Masukkan bilangan positif (<0 untuk mengakhiri):"
myStack = Stack() # Membuat stack baru (program di halaman berikut)
value = int(input( PROMPT ))
while value >= 0 : # Memasukkan satu per satu
    myStack.push( value )
value = int(input( PROMPT ))
while not myStack.isEmpty() : # Mengeluarkan satu per satu
    value = myStack.pop()
print( value )