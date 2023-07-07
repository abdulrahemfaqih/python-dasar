import os
os.system('cls')

print('buatlah program membuat deret bilangan ganjil dan genap, dimana jumlah bilangan bilangan dari inputan user, ouput yang anda kerjakan harus sama dengan contoh yang saya berikan!\n')

awal = int(input('masukkan angka awal = '))
batas = int(input('masukkan angka akhir = '))

for i in range(awal,batas +  1):
  if i % 2 == 1:
    print(i, end = ' ')
print('= deret ganjil')
 
for i in range(awal,batas +  1):
  if i % 2 == 0:
    print(i, end = ' ')
print('= deret genap\n')





 




