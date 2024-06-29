class PriorityQueue(object):
    def __init__(self):
        """Membuat antrian prioritas kosong."""
        self.qlist = []  # List untuk menyimpan antrian prioritas.

    def __len__(self):
        """Mengembalikan jumlah elemen di dalam antrian prioritas."""
        return len(self.qlist)  # Gunakan len() untuk menghitung elemen

    def print(self):
        for i in range(len(self.qlist)):
            print(self.qlist[i].data)

    def isEmpty(self):
        """Mengembalikan True jika antrian prioritas kosong, False jika tidak."""
        return len(self) == 0  # Gunakan len() untuk mengecek elemen

    def enqueue(self, data, priority):
        """Memasukkan data baru dengan prioritas tertentu ke dalam antrian."""
        entry = _PriorityQEntry(data, priority)  # Memanggil object _PriorityQEntry
        self.qlist.append(entry)


    def dequeue(self):
        """Menghapus dan mengembalikan elemen dengan prioritas tertinggi 
           dari antrian prioritas."""
        # Mencari indeks elemen dengan prioritas tertinggi
        highest_priority_index = 0
        for i in range(1, len(self.qlist)):
            if self.qlist[i].priority > self.qlist[highest_priority_index].priority:
                highest_priority_index = i

        # Menghapus dan mengembalikan elemen dengan prioritas tertinggi
        return self.qlist.pop(highest_priority_index)
    
    def getFrontMost(self):
        if not self.isEmpty():
            highest_priority_index = 0
            for i in range(1, len(self.qlist)):
                if self.qlist[i].priority < self.qlist[highest_priority_index].priority:
                    highest_priority_index = i
        else:
            return "Tidak ada nilai untuk didapat"            

        # Menghapus dan mengembalikan elemen dengan prioritas tertinggi
        return self.qlist[highest_priority_index - 1].data
    
    def getRearMost(self):
        if not self.isEmpty():
            lowestIndex = 0
            for i in range(1, len(self.qlist)):
                if self.qlist[i].priority > self.qlist[lowestIndex].priority:
                    lowestIndex = i
        return self.qlist[lowestIndex - 1].data            

class _PriorityQEntry:
    """Entry untuk menyimpan data dan prioritas di dalam PriorityQueue."""
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

pq = PriorityQueue()
pq.enqueue("Kerjakan laporan penting (Prioritas 1)", 1)
pq.enqueue("Rapikan meja kerja (Prioritas 2)", 2)
pq.enqueue("Balas email (Prioritas 3)", 3)



print("sebelum deq " + pq.getFrontMost() + "\n")
pq.print()

pq.dequeue()

print("setelah Dequ " + pq.getFrontMost() + "\n")
pq.print()

print(pq.getRearMost())




