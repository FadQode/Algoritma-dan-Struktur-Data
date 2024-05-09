def persegi(x, y):
    square = ""
    for i in range(x):
        square = "@"
        for j in range(y - 1):
            if i == 0 or j == y-2 or i == x-1:
                square += "@"
            else:    
                square += " "
        print(square)

persegi(4, 5)