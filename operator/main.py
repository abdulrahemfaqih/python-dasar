# '''PERULANGAN'''

# '''
# dalam perulangan itu dua macam yaitu 
# 1. for loop
# 2. while loop
# '''
import os
os.system('cls')

# FORLOOP 

# for kondisi:
#   aksi 

# for loop dengan list
print('\n')
angka2 = [1,2,3,4,5,6,7,8,9,10]
print (angka2)

for i in angka2 :
    print(f'i sekarang -->{i}')

print('\nberakhir\n')

# for loop dengan range 

angka1 = range(20,40)

for i in angka1:
    print(f'i sekarang -->{i}')


# menggunakan string

data_str = 'kamu ada dimana?'

for huruf in data_str:
    print(huruf)

print('\n')

# WHILE LOOP

angka = 1
print(f'angka sekarang --> {angka}')


while angka < 10 :
    angka *= 2
    print(f'angka sekarang --> {angka}')
    print('halo')
print('wes ta')