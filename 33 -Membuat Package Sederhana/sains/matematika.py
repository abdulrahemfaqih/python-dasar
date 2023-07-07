'''modul matematika'''

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

def pangkat(angka,pangkat):
    pangkat = angka**pangkat

    return pangkat

    
