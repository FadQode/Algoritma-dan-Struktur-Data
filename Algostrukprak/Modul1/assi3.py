def pisahHuruf(kalimat):
    hurufVokal = ["a", "i", "u", "e", "o"]
    konsonan = 0
    vokal = 0
    huruf = 0
    for i in range(len(kalimat)):
        if kalimat[i] in hurufVokal:
            vokal += 1
        else:
            konsonan += 1
        huruf += 1    
    return (huruf, vokal, konsonan)        

print(pisahHuruf("surakarta"))

