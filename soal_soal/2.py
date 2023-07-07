import os
os.system('cls')

# print('buatlah program untuk mencari index dari suatu huruf pada kalimat, dimana kalimat tersebut merupakan inputan dari user (huruf besar dan kecil di anggap sama)\n')

# a = input('masukkan kalimat = ')
# b = input('inputkan huruf yang mau dicari = ')

# x = 0
# for i in range(len(a)):
#   if  a[i] == b or a.upper()[i] == b.upper():
#     x += 1
#     print(f'\nhuruf {b} atau huruf {b.upper()} ke - {x} : index ke - {i}\n')



awal = int(input('angka awal = '))
akhir = int(input('angka akhir = '))

print('deret bilangan kuadrat')
for i in range(awal,akhir + 1):
  print(i*i,end = ' ')
  
print()
print()












