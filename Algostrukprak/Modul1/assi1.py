def segitigaSiku(x):
    triangle = ""
    for i in range(x):
        triangle = "*"
        for j in range(i):
            triangle += "*"
        print(triangle)

segitigaSiku(5)