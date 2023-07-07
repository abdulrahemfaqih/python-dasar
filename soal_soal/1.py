import os
os.system('cls')

print('Buatlah program untuk menampilkan bilangan-bilangan pembagi yang sama (antara dua buah bilangan, yang merupakan inputan dari user), dan dari bilangan pembagi tersebut\n')

print()
angka1 = int(input('angka pertama = '))
angka2 = int(input('angka kedua = '))
x = 0
for i in range(1, angka1 + 1):
  if angka1 % i == 0 and angka2 % i == 0:
    x += 1 
    print(f'pembagi yang sama - {x} = {i}')
    j = i
print(f'\npembagi yang sama terbesar adalah = {j}\n')




for i in range(1,10):
  print(i)