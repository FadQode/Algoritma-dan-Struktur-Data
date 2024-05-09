class Node:
    """Menginisialisasi class node yang akan menjadi isi dan object dari class llinlist"""
    def __init__(self, data=None):
        """Node memiliki 2 properti yaitu data dan next"""
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False    

    def insertAtBeginning(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            if self.head.prev == None:
                self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def PrintLinkedList(self):
        """Mengunjungi setiap nilai object node dalam linked list dan menampilkan nilai properti datanya"""
        #pengunjungan dimulai dari head 
        printval = self.head
        #selanjutnya selama printval masih memiliki nilai
        while printval.next is not None:
            #menampilkan data dari printval yang berisi object node
            print (printval.data)
            #menuju object node selanjutnya
            printval = printval.next  
        print (printval.data)
        while printval is not None:
            print(printval.data)
            printval = printval.prev    


        # while printval is not None:
        #     print(printval.data)
        #     printval = printval.prev


a = [1, 2, 3, 4, 5]              
advLL = DoublyLinkedList()
advLL2 = DoublyLinkedList()

for i in range(0, len(a)):
    advLL.insertAtBeginning(a[i])
    advLL2.insertAtEnd(a[i])
print("ini Begining")

advLL.PrintLinkedList()   
print("ini the end")

advLL2.PrintLinkedList()

