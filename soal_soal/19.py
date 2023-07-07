import os
os.system('cls')

'''program menampilkan bilangan ganjil dan genap pada sebuah list'''

# fungsi function filter adalah

awal  = int(input('masukkan angka awal = '))
akhir = int(input('masukkan angka akhir = '))

angka2 = []
for i in range (awal, akhir + 1):
  angka2.append(i)
print(angka2)

def genap(x):
  return x % 2 == 0
def ganjil(x):
  return x % 2 != 0

print('')
print(list(filter(ganjil,angka2)))
print(' ')
print(list(filter(genap,angka2)))
print(' ')
