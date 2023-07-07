# module matematika 




def tambah(*args):
    hasil = 0

    for data in args:
        hasil = hasil + data

    return hasil

def kurang(*args):
    hasil = 0

    for data in args:
        hasil = hasil - data

    return hasil

def kali(*args):
    hasil = 1

    for data in args:
        hasil = hasil * data

        
    return hasil

def bagi(*args):
    hasil = 1

    for data in args:
        hasil = hasil / data

        return hasil 

def pangkat(bilangan, pangkat):
    hasil = bilangan ** pangkat
    return hasil 
