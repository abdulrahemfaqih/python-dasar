import os
os.system('cls')

awal = int(input('masukkan angka awal = '))
akhir = int(input('masukka angka akhir = '))

deret = []

for i in range(awal, akhir + 1):
  deret.append(i)

def pangkat(pangkat):
  return pangkat*pangkat

print(' ')
print(list(map(pangkat,deret)))

print(' ')
  
