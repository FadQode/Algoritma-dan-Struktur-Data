def paliCheck(str):
    normal = ([*str])
    rev = []
    for i in range(len(normal)):
        rev.append(normal[-1])
    for i in range(len(rev)):
        if rev[i] != normal[i]:
            return "Not Palindrom"    
    return "palindrom"
print(paliCheck("kasur rusak"))
    
        

    