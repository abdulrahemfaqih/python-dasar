import os
os.system('cls')

'''
1. Buatlah program untuk menampilkan bilangan kelipatan 7, dimulai dari 1 sampai batas yang merupakan inputan user

2. Buatlah program untuk menghitung jumlah sederet bilangan kelipatan 7 berurut yang dimulai dari 1 hingga angka inputan user

3. buatlah program menghitung jumlah sederet bilangan berpangkat 3 , dimulai dari 1 gingga angka inputan user

4. menampilkan deret bilangan faktorial, dimana batas deretnya ditetukan oleh user  
'''


'''JAWABAN'''


# # 1.
# print('\nmenampilkan bilangan kelipatan 7 dari 1\n')
nilai_akhir = int(input('masukkan nilai batas akhir = '))
start = 1
deret = []

for i in range(start, nilai_akhir + 1):
    if i % 7 == 0:
        deret.append(i)

print(f'bilangan kelipatan 7 hingga {nilai_akhir}\n{deret}\n')


# 2. 
# print('\nmenghitung jumlah sederet bilangan kelipatan 7\n')
# angka_akhir = int(input('masukkan batas akhir = '))
# start = 1
# jumlah = 0
# deret = []

# for i in range(start, angka_akhir + 1):
#     if i % 7 == 0: 
#         deret.append(i)
#         jumlah += i

# print(f'\nderet bilangan kelipatan 7 hingga {angka_akhir}\n{deret}') 
# print(f'jumlah dari semua bilangan = {jumlah}\n')


# 3. 
# print('\nmenampilkan deret bilangan pangkat 3\n')

awal = int(input('masukkan angka awal = '))
batas = int(input('masukkan batas angka = '))

jumlah = 0
deret = []

for i in range(awal, batas + 1):
    pangkat = i ** 3
    deret.append(pangkat)
    jumlah += pangkat
print(f'deret pangkat 3 = {deret}')
print(f'jumlah = {jumlah}\n')



# 4. 
print('\nmenampilkan deret bilangan faktorial\n')
n = int(input('masukkan nilai n = '))
faktorial = 1

for i in range(1, n + 1 ):
    faktorial *= i
    print(f'{i}!  = {faktorial}')
























