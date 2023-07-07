# for loop

# for kondisi :
#   aksi 
import os
os.system('cls')
# ini dengan list
angka2 = [1,2,3,4,5,6]
print(angka2)

for i in angka2 :
  print(f'i sekarang --> {i}')
print('berakhir\n')

# ini dengan range 
angka1 = range(5) 

for i in angka1 :
  print(f'i sekarang --> {i}')
print('berakhir\n')

angka1 = range(1,5)

for i in angka1 :
  print(f'i sekarang --> {i}')
print('berakhir\n')


# menggunakan string 

data_str = 'rumah mu dimana?'

for huruf in data_str :
  print(huruf)
print('berakhir')