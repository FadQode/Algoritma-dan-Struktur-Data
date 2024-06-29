class Node:
    """Menginisialisasi class node yang akan menjadi isi dan object dari class llinlist"""
    def __init__(self, data=None):
        """Node memiliki 2 properti yaitu data dan pointer"""
        self.data = data
        self.pointer = None

class LinkedList:
    """Menginisialisasi class yang berstruktur data linked list"""
    def __init__(self):
        """Class ini memiliki suatu properti yaitu head(kepala linlist)"""
        self.head = None

    def search(self, data):
        printval = self.head
        #selanjutnya selama printval masih memiliki nilai
        while printval.data != data:
            #menampilkan data dari printval yang berisi object node
            #menuju object node selanjutnya
            printval = printval.pointer
        print(printval.data)   

    def PrintLinkedList(self):
        """Mengunjungi setiap nilai object node dalam linked list dan menampilkan nilai properti datanya"""
        #pengunjungan dimulai dari head 
        printval = self.head
        #selanjutnya selama printval masih memiliki nilai
        while printval is not None:
            #menampilkan data dari printval yang berisi object node
            print (printval.data)
            #menuju object node selanjutnya
            printval = printval.pointer   
        return"Fadhil Erdya Qashmal\n"     

    def sumTraverse(self):        
        """Mengunjungi setiap nilai object node dalam linked list dan menampilkan nilai properti datanya"""
        #pengunjungan dimulai dari head 
        printval = self.head
        #variabel untuk menyimpan hasil penjumlahan 
        sum = 0
        #selanjutnya selama printval masih memiliki nilai
        while printval is not None:
            #MEnambahkan setiap data lalu disimpan dalam sum
            sum += printval.data
            #menuju object node selanjutnya
            printval = printval.pointer
        print("Fadhil Erdya Qashmal")     
        return f"Jumlah semua data adalah {sum}"           
            

    def AtBegining(self,newdata):
        """Menambah(mengganti) object node baru pada head(bagian terdepan) dari object linked list"""
        #membuat suatu object node bary
        NewNode = Node(newdata)
        #hubungkan pointer object node baru ke head lama
        NewNode.pointer = self.head
        #ubah head menjadi object node baru
        self.head = NewNode

    def AtEnd(self, newdata):
        """Menambah object node pada akhir object linlist"""
        #membuat object node baru
        NewNode = Node(newdata)
        #melakukan traversal mengunjungi setiap object node hingga akhir(nilai object none)
        laste = self.head
        while(laste.pointer != None):
            laste = laste.pointer
        #setelah none ubah pointer node terakhir yang sebelumnya kosong menjadi node baru    
        laste.pointer=NewNode

    def Inbetween(self,middle_node,newdata):
        """Menambah Object node ditengah tengah object linlist"""
        #lakukan traversal hingga isi properti data node sama dengan parameter
        printval = self.head
        while printval.data != middle_node:
            printval = printval.pointer
        #buat satu object node baru 
        NewNode = Node(newdata)
        #hubungkan pointer node baru ke pointer node tengah sebelumnya
        NewNode.pointer = printval.pointer
        #hubungkan pointer node tengah sebelumnya ke node baru
        printval.pointer = NewNode

    def RemoveNode(self, Removekey):
        """Menghilangkan suatu object node di dalam object linked list"""
        #Melakukan Traversal mencari node yang memiliki data dengan nilai yang sama dengan Remove Key
        HeadVal = self.head
        #Mengecek apakah HeadVal sudah terisi
        if (HeadVal is not None):
            #Mengecek apakah data head sama dengan data yang ingin di remove
            if (HeadVal.data == Removekey):
                #jika iya maka head akan diganti ke node selanjutnya
                self.head = HeadVal.pointer
                #Head akan di remove
                HeadVal = None
                return
        #selama headval belum kosong lakukan traversal    
        while (HeadVal is not None):
            #jika ditemukan data yang sama dengan remove key
            if HeadVal.data == Removekey:
             #keluar dari perulangan
             break
            #jika tidak perulangan dan traversal akan berlanjut
            prev = HeadVal
            HeadVal = HeadVal.pointer
        #jika headval tidak ditemukan alias none, program selesai
        if (HeadVal == None):
            return
        #setelah keluar dari perulangan pointer nilai sebelumnya akan dihubungkan ke pointer headval
        prev.pointer = HeadVal.pointer
        #object node headval akan di remove
        HeadVal = None     
        return 
    


