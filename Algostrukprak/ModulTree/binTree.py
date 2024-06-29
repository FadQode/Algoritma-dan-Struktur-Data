class _SimpulPohonBiner(object):
    def __init__( self, data ):
        self.data = data
        self.kiri = None
        self.kanan = None


def treesize(branch):
   if branch is None:
     return 0
   return 1 + treesize(branch.kiri) + treesize(branch.kanan)

def print_branch(node, level=0):
   if node is None:
     return
   print(f"Level {level}: {node.data}")
   print_branch(node.kiri, level + 1)
   print_branch(node.kanan, level + 1)

def find_depth(node):
  if node is None:
    return -1 
  return 1 + max(find_depth(node.kiri), find_depth(node.kanan))

         


root = _SimpulPohonBiner(1)
left = _SimpulPohonBiner(2)
root.kiri = left
left.kanan = _SimpulPohonBiner(3)
root.kanan = _SimpulPohonBiner(4)
right = root.kanan
right.kiri = _SimpulPohonBiner(5)


"""
            1                           
          /   \                         
         2      4
          \     /
            3   5

"""


# Membuat simpul-simpul dan mengisi data
A = _SimpulPohonBiner('Ambarawa')
B = _SimpulPohonBiner('Bantul')
C = _SimpulPohonBiner('Cimahi')
D = _SimpulPohonBiner('Denpasar')
E = _SimpulPohonBiner('Enrekang')
F = _SimpulPohonBiner('Flores')
G = _SimpulPohonBiner('Garut')
H = _SimpulPohonBiner('Halmahera Timur')
I = _SimpulPohonBiner('Indramayu')
J = _SimpulPohonBiner('Jakarta')

# Menghubungkan simpul ortu-anak
A.kiri = B
A.kanan = C
B.kiri = D
B.kanan = E
C.kiri = F
C.kanan = G
E.kiri = H
G.kanan = I


"""
        A
        / \
      B     C
      / \   / \
    D   E F   G
        /     \ 
        H       I

"""

print(treesize(left))
print_branch(left)
print(find_depth(root))

print(treesize(A))
print_branch(A)
print(find_depth(A))


"""
1. jumlah node = 2^(h+1) - 1
n = jumlah node
A. n = 10
10 = 2^(h+1) - 1
h = 3
max level = 3
min level = 9

B. n = 35
2 ^(h+1) - 1 = 35
h = 5
min level = 34
C. n = 76

2^(h+1) - 1 = 76
h = 6
max level = 6
min level = 75

D. n = 345
2^(h+1) - 1 = 345
max level = 8
min level = 344

2. C(5, 5) = 5! / 5!(5-5)!
= 5! / 5!0!
= 120 / 1
= 120
"""