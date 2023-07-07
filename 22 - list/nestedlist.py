# list bersarang 

data1= [1,2,3]
data2 = [4,5,6]

list1 = [1,2,3,4,5,6]
print(f'\nlist biasa = {list1}')

list2 = [data1, data2, list1]
print(f'nested list = {list2}')

# contoh penggunaan list peserta

peserta1 = ['erick', 25, 'laki-laki']
peserta2 = ['sumarni', 21, 'wanita']
peserta3 = ['sumarto', 23, 'laki-laki']

list_peserta = [peserta1, peserta2, peserta3]
print(f'list peserta = {list_peserta}\n')

for peserta in list_peserta:
  print(f'nama\t : {peserta[0]}')
  print(f'umur\t : {peserta[1]}')
  print(f'gender\t : {peserta[2]}\n')


# dengan refenrence

list_copy = list_peserta.copy()
print(f'peserta = {list_copy}\n')
peserta1[0]= 'farish'
print(f'peserta = {list_copy}\n')
print(f'peserta = {list_peserta}\n')
# --> akan di bahas di deep copy nested list