import os
os.system('cls')


angka = int(input('masukkan angka = '))
faktor = 0
for i in range(1, angka + 1):
  if angka % i == 0:
    faktor += 1
  
if faktor ==2:
  print(f'{angka} bilangan prima')
else:
  print('bukan')

  