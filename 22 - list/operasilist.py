

data = [1,2,3,4,5,6,7,8,1,2,3,4,5,1,2,3,4,5,6,7,8,1,2,3,4,5,5,6,7,1,2,3,4,5,6,7,8,9]
data_nama = ['farish', 'buccok', 'kivlan', 'rico', 'holis']

print(f'data angka =\n{data}')

# count data

jumlah_data1 = data.count(1)
jumlah_data2 = data.count(2)
jumlah_data3 = data.count(3)
jumlah_data4 = data.count(4)
jumlah_data5 = data.count(5)

print(f'jumlah data 1 = {jumlah_data1}')
print(f'jumlah data 2 = {jumlah_data2}')
print(f'jumlah data 3 = {jumlah_data3}')
print(f'jumlah data 4 = {jumlah_data4}')
print(f'jumlah data 5 = {jumlah_data5}')

# menampilkan posisi data (index)

index_buccok = data_nama.index('buccok')
index_rico = data_nama.index('rico')

print(f'index nama buccok = {index_buccok}')
print(f'index nama rico = {index_rico}')

# mengurutkan list menggunakan (sort)

print(f'data angka sebelum di urutkan =\n{data}')
data.sort()
print(f'data angka setelah di urutkan =\n{data}')

print(f'data nama sebelum di urutakan :\n{data_nama} ')
data_nama.sort()
print(f'data nama sesudah di urutkan :\n{data_nama}')

# membalikkan urutkan list memggunakan (reverse)

data.reverse()
data_nama.reverse()
print(f'data setelah di inverse =\n{data} \n{data_nama}')





import os
os.system('cls')
print()


# menghitung panjang list -> len
data_angka = [1,3,4,5,6,34,47]
print(data_angka)
print('panjang data =',len(data_angka))

print()
# menambah nilai ke dalam list -> append
data_angka = '1234567997257'
list_angka = []
for i in data_angka:
  list_angka.append(int(i))
print(list_angka)
print(f'memiliki panjang data = {len(list_angka)}')
  

print()


listAngka = [1,6,7,4,8,3,5]
print(listAngka)
listAngka.sort()
print(f'list angka after sort = {listAngka}')
listAngka.reverse()
print(f'list angka after reverse = {listAngka}')



print()
