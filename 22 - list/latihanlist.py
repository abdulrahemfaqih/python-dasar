# program list buku 
# list_buku = []
# while True:
#   print('\n              MASUKKAN DATA BUKU')
#   judul        = input('Judul     : ')
#   penulis      = input('Penulis   : ')
#   Tahun_terbit = int(input('Tahun \t  : '))

#   dataBuku     = [judul, penulis, Tahun_terbit]
#   list_buku.append(dataBuku)
  
#   print('\n\n','-'*40)
#   for index,buku in enumerate(list_buku):
#     print(
#       f'{index+1}| {buku[0]} {buku[1]} {buku[2]}'
#       )

#   print('\n\n','-'*40)
#   isLanjut = input('apakah dilanjutkan (y/n): ')

#   if isLanjut == 'n':
#     break



# nama = input('masukkan : ')
# n = []
# m = []

# for x in range(len(nama)):
#   n.append(nama[x])
# print(n)
# for i in range(len(nama) -1,-1,-1):
#   m.append(nama[i])

# print(m)



import os
os.system('cls')


# remove 
data_angka = [1,2,3,4,5,6,7,8]
while True:
  print(data_angka)
  hapus = int(input('hapus data = '))
  data_angka.remove(hapus)
  tanya = input('mau menghapus lagi? y/n: ')
  if tanya == 'n':
    print(data_angka)
    break
print()

# pop 
data_angka = [1,2,3,4,5]
print(data_angka)
for angka in range(len(data_angka)):
  data_angka.pop()
print(f'data angka setelah di pop = {data_angka}')

print()




