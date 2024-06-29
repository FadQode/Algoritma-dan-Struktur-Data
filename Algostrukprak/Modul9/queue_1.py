class Queue(object):
    def __init__(self):
        """Membuat antrian kosong."""
        self.qlist = []  # List untuk menyimpan antrian.

    def isEmpty(self):
        """Mengembalikan True jika antrian kosong, False jika tidak."""
        return len(self) == 0  # Gunakan len() untuk mengecek elemen

    def __len__(self):
        """Mengembalikan jumlah elemen di dalam antrian."""
        return len(self.qlist)  # Gunakan len() untuk menghitung elemen

    def enqueue(self, data):
        """Memasukkan data baru ke akhir antrian."""
        self.qlist.append(data)

    def dequeue(self):
        """Menghapus dan mengembalikan elemen terdepan dari antrian."""
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)
    
    def getFrontMost(self):
        return self.qlist[0]
    
    def getRearMost(self):
        return self.qlist[len(self.qlist) -1]
    
myQueue = Queue()

# Menambahkan elemen ke antrian
myQueue.enqueue("Hello")
myQueue.enqueue("World")
myQueue.enqueue("!")

myQueue.enqueue("Ini Yang Paling Belakang")

print(myQueue.getFrontMost())
print(myQueue.getRearMost())