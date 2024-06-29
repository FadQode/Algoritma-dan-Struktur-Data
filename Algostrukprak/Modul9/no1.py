class Stack(object):
    def __init__(self):
        """Membuat stack kosong."""
        self.items = []  # List untuk menyimpan stack.

    def isEmpty(self):
        """Mengembalikan True kalau kosong, selain itu False."""
        return len(self) == 0  # Gunakan len() untuk menghitung elemen

    def __len__(self):
        """Mengembalikan banyaknya item di stack."""
        return len(self.items)  # Gunakan len() untuk menghitung elemen

    def peek(self):
        """Mengembalikan nilai posisi atas tanpa menghapus."""
        if self.isEmpty():
            raise Exception("Stack kosong. Tidak bisa diintip")  # Gunakan exception
        return self.items[-1]

    def pop(self):
        """Mengembalikan nilai posisi atas lalu menghapus."""
        if self.isEmpty():
            raise Exception("Stack kosong. Tidak bisa di-pop")  # Gunakan exception
        return self.items.pop()

    def push(self, data):
        """Mendorong item baru ke stack."""
        self.items.append(data)

def hexacize(num):    
    hexa = ""
    s = Stack()
    while num > 0:
        s.push(num % 16)
        num //= 16
    while not s.isEmpty():
        hexa += digitToHexa(s.pop())

    return hexa

def digitToHexa(d):
    if d < 10:
        return str(d)
    else:
        return chr(ord('A') + d - 10)                           


print(hexacize(12))
print(hexacize(31))
print(hexacize(229))
print(hexacize(255))
print(hexacize(31519))