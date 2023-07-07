import os
os.system('cls')


def tambah(*data):
# data tipenya adalah tupple, dan dia bisa diiterasi/perulangan
    ouput = 0
    
    for angka in data:
        ouput += angka
    
    print(ouput)

tambah(5,10,15,20,25,30)

print()