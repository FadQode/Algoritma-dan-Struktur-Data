
def tahunKabisat(tahun: int)-> int:
    check = tahun / 4
    if tahun % 4 == 0 :
        if check % 100 !=  0 :
            return"tahun kabisat"
                #diseleksi lagi jika sisanya 0
        else :
            if tahun % 400 == 0 :
                return "tahun kabisat"
            else :
                return "bukan tahun kabisat"

    else:
        return "bukan tahun kabisat"