def formatRupiah(masukkan: int)-> int:  
    return "Rp. {:,.0f}".format(masukkan)

print(formatRupiah(100000))