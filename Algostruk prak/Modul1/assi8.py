def isAinB(kalimat1:str, kalimat2:str)-> str:
    if kalimat1 in kalimat2:
        return True
    else:
        return False 



kal1 = "kita"
kal2 = "Ikuyo kita pernah jadi waifu saya"
print(isAinB(kal1,kal2)) 