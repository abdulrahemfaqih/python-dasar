import os
os.system('cls')

print('buatlah program hitung mundur menggunakan perulangan for dan while, dimana bilangan  tersebut merupakan inputan dari user\n')


awal = int(input('masukkan angka awal : '))
akhir = int(input('masukkan anga akhir: '))

while awal >= 1:
  print(awal,end = ' ')
  awal = awal - 1
  if awal == akhir - 1 :
    break


  
print('\n')

# for i in range(awal,akhir-1,-1):
#   prin5
# t(i)

'''perulangan dari angka awal - akhir'''
awal = int(input('awal = '))
akhir = int(input('akhir = '))

while awal <= akhir:
  print(awal,end=' ')
  awal += 1
  
print('\n')

  