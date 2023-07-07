def tambah(*angka):
    hasil = 0

    for i in angka:
        hasil += i

    return hasil

def kali(*angka):
    hasil = 1

    for i in angka:
        hasil *= i

    return hasil

def pangkat(bilangan,pangkat):
    pangkat = bilangan**pangkat
    return pangkat
    
