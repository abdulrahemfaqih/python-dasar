# OPERATION  


data = ['kivlan', 'Febrianu', 'Farish', 'Andre' , 'Anam']

data0 = data[0]
print(f'data pertama - index 0 = {data0} ')


data4 = data[4]
print(f'data keempat - Index 3 = {data4} ')

data2_4 = data[2:4]
print(f'data kedua - empat = {data2_4} ')

dataTerakhir = data[-1]
print(f'data terakhir = {dataTerakhir} ')

# Mengambil info jumlah dalam list

jumlahData = len(data)
print(f'jumlah data = {jumlahData}')



## Manipulasi Data list 

# menambah item pada list sesuai posisi
print(f'data sebelum ditambah ->\n{data}')

data.insert (2,'Habib') # -->menambah item habib di posisi ke kedua- index 3
print(f'data sesudah ditambah ->\n{data}')

# menambah item di akhir list
data.append('Akbar')
print(f'data terbaru -> {data}')

# menambah list dengan list 
dataBaru = ['Wahyudi', 'Mahreza', 'Alif', 'Navy']
data.extend(dataBaru)
print(f'data setelah di gabung -> {data}')

# merubah data --> misal mengubah data ke 2 menajdi sahrul
data[2] = 'sahrul'
print(f'data paling baru {data} ')



# import os
# os.system('cls')

# # insert -> menambahkan data sesuai posisi
# data_angka = [1,2,3,4,5,7]
# print(data_angka)
# tambah_list = input('masukkan data = ')
# posisi = int(input('posisi = '))
# if tambah_list == int:
#   data_angka.insert(posisi,int(tambah_list))
#   print('setelah di insert = ',data_angka)
# else:
#   data_angka.insert(posisi,tambah_list)
#   print('setelah di insert = ',data_angka)
# print()  
# # extend -> menambah list dengan list
# list1 = input('masukkan data angka = ').split(' ')
# data1 = list(list1) # list() -> membuat list
# print(data1)
# list2 = input('masukkan data angka = ').split(' ')
# data2 = list(list2)
# print(data2)
# data1.extend(data2)
# print(f'data setelah di extend = {data1}')
# print()




