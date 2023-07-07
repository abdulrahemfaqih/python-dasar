import os
os.system('cls')

awal = int(input('masukkan angka awal = '))
akhir = int(input('masukkan angka akhir = '))

ganjil = []
genap = []

for x in range(awal, akhir + 1):
    if x%2 == 0:
       genap.append(x)
    else :
        ganjil.append(x)

print(f'ganjil = {ganjil}')
print(f'genap = {genap}')


