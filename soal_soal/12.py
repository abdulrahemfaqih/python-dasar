import os
os.system('cls')
'''
1. menampilkan bilangan 1 - 100 yang habis dibagi dengan 2 dan habis dibagi 3
2. penjumlahan deret ke-n, tetapi yang dijumlahkan adalah bilangan yang ganjil saja
'''

'''jawaban'''

# 1. 
n = 100

deret = []
for i in range(1,n):
    if i % 2  == 0 and i % 3 == 0:
        deret.append(i)

print(f'deret bilangan 1-100 yang habis dibagi 3 dan 2 =\n{deret}')


# 2. 

n = int(input('masukkan n = '))
deret = []
jumlah = 0

for i in range(1,n + 1):
    if i % 2 == 1:
        deret.append(i)
        jumlah += i

print(f'deret bilangan = {deret}')
print(f'jumlah = {jumlah}')
