'''
                                                  by: ARF
         MENGUBAH MEMBER DI DALAM NESTED LIST
'''

data1 = [1,2]
data2 = [3,4]

data_gabungan = [data1, data2]
data_gabungan_copy = data_gabungan.copy()
print(f'\ndata \t\t= {data_gabungan}')
print(f'data copy \t= {data_gabungan_copy}\n')


# mengambil data dari nestedlist
print('----MENGAMBIL DATA DARI NESTED LIST----')

data = data_gabungan[0]
print(f'data \t= {data}')
data = data_gabungan[0][1]
print(f'data 0 \t= {data}\n')

# Address 
print('          ----ADDRESS----')
print(f'address asli = {hex(id(data_gabungan))}')
print(f'address copy = {hex(id(data_gabungan_copy))}\n')

print('      -- ADDRESS MEMBER KE-1--')
print(f'address asli = {hex(id(data_gabungan[0]))}')
print(f'address copy = {hex(id(data_gabungan_copy[0]))}\n')


data_gabungan[0][0] = 10
print(f'\ndata \t\t= {data_gabungan}')
print(f'data copy \t= {data_gabungan_copy}\n')

# menggunakan deepcopy
print('    --- MENGGUNAKAN DEEPCOPY ---')

from copy import deepcopy

data_gabungan = [data1, data2]
data_gabungan_deepcopy = deepcopy(data_gabungan)

print('          ----ADDRESS----')
print(f'address asli      = {hex(id(data_gabungan))}')

print(f'address deep copy = {hex(id(data_gabungan_deepcopy))}\n')

print('     -- ADDRESS MEMBER KE-1--')
print(f'address asli = {hex(id(data_gabungan[0]))}')
print(f'address copy = {hex(id(data_gabungan_deepcopy[0]))}\n')

# mengubah member menggunakan deepcopy
print('-- MENGUBAH MEMBER MENGGUNAKAN DEEPCOPY --')
data_gabungan_deepcopy[0][1] = 100
data_gabungan_copy[0][0] = 1

print(f'data_gabungan           = {data_gabungan}')
print(f'data gabungan copy      = {data_gabungan_copy}')
print(f'data gabuangan deepcopy = {data_gabungan_deepcopy}')