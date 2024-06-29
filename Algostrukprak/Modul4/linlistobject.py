from linkedList import *

data = LinkedList()
print("Ini At Beginning")
data.AtBegining(9)
data.AtBegining(2)
data.AtBegining(3)
print(data.PrintLinkedList())


print("ini At End")
data.AtEnd(7)
data.AtEnd(10)
print(data.PrintLinkedList())

print("Ini in Between")
data.Inbetween(2, 6)
data.Inbetween(3, 5)
data.Inbetween(9, 12)
print(data.PrintLinkedList())

print("Ini Remove node")
data.RemoveNode(12)
data.RemoveNode(10)
print(data.PrintLinkedList())

print("ini Traversal")
print(data.PrintLinkedList())

print("ini Traversal penjumlahan")
print(data.PrintLinkedList())
print(data.sumTraverse())

print("ini search node")
print(data.search(7))