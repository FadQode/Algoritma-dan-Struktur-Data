def umsPython(i: int)-> int:
        if i % 3 == 0 and i % 5 == 0:
            return "python UMS"
        elif i % 3 == 0:
            return "python"
        elif i % 5 == 0:
            return "ums"
        else:
            return i

for i in range(1,101):
     print(umsPython(i))