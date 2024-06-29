import numpy

def cekIsiMatriks(arr: list) -> list :
    x = 0
    y = len(arr)
    for i in range(len(arr)):
        if len(arr[i]) != len(arr[i - 1]):
            return "terjadi ketidak konsistenan"
        for j in range(len(arr[i]) ):
            if not isinstance(arr[i][j], int):
                return "Terdapat instance bukan integer dalam matriks"

        x = len(arr[i])
    return f"matriks berukuran {x}x{y}"    

def jumlahDuaMatriks(arr1, arr2):
    newMatriks = []
    if cekIsiMatriks(arr1) != cekIsiMatriks(arr2):
        return "ukuran matriks tidak sama atau ada alasan lain"
    else:
        for i in range(0, len(arr1)):
            childMatriks = []
            for j in range(0, len(arr1[i])):
                sum = arr1[i][j] + arr2[i][j]
                childMatriks.append(sum)
            newMatriks.append(childMatriks)   
    return newMatriks         

def perkalianMatriks(arr1, arr2):
    if cekIsiMatriks(arr1) != cekIsiMatriks(arr2):
        return "ukuran matriks tidak sama atau ada alasan lain"
    else:
        newMatriks = [[0 for a in range(len(arr2[0]))] for b in range(len(arr1))]
        for i in range(0, len(arr1)):
            for j in range(0, len(arr1[0])):
                for k in range(0, len(arr2)):
                    newMatriks[i][j] += arr1[i][k] * arr2[k][j]
            """child matriks = [[3 4 4]  
                                [14 16 8]
                                [27 30 12]  [
                            [3,4,4], 
                            [7,8,4], 
                            [9,10,4]]"""
        return newMatriks   
        


def buatNol(x, y=0):
    if y != 0:
        newMatriks = [[0 for a in range(y)] for b in range(x)]
    else:
        newMatriks = [[0 for a in range(x)] for b in range(x)] 
    return newMatriks

def buatIdentitas(m):
    newMatriks = [[0 for a in range(m)] for b in range(m)]
    for a in range(len(newMatriks)):
        newMatriks[a][a] = 1
    return newMatriks        

# def determinant(arr):
#      if len(arr) != len(arr[0]):
#             return "Matriks bukan bujurSangkar"
#      else:
#          return numpy.linalg.det(arr)
def matrix_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        row = len(matrix)
        col = len(matrix[0])
        sign = -1
        result = 0
        row1 = [matrix[0][i] * (sign ** i) for i in range(col)]
        print(row1)
        for x, y in enumerate(row1):
            print(x,y)
            mat = matrix[:][1:]
            print(mat)
            sub_matrix = [[mat[i][j] for j in range(col) if j != x] for i in range(row - 1)]
            result += y * matrix_determinant(sub_matrix)
        return result

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(cekIsiMatriks([[1,2],
                     [6,4],
                     [8,]]))

print(jumlahDuaMatriks([[1,2,3],
                        [6,4,4],
                        [7,3,5]], [
                            [3,4,4], 
                            [7,8,4], 
                            [9,10,4]]))
print(perkalianMatriks([[1,2,3],
                        [6,4,4],
                        [7,3,5]], [ [3,4,4], 
                            [7,8,4], 
                            [9,10,4]]))
# print(determinant([[1,2,3],
#                     [6,4,4],
#                     [7,3,5]]))
print(matrix_determinant(matrix))
print(matrix_determinant([[1,2,3],
                        [6,4,4],
                        [7,3,5]]))


