import os
os.system('cls')

# lambda function 

def fungsi_kuadrat(angka):
    return angka**2

print(f'hasil fungsi kuadarat = {fungsi_kuadrat(4)}')

'''dengan fungsi lambda semuanya dapat dipersingkat'''
# output = lambda - argument: expression

fungsi_kuadrat = lambda angka: angka**2
print(f'hasil dari lambda kuadarat = {fungsi_kuadrat(100)}')

fungs_kali = lambda a,b : a*b

print(f'hasil {fungs_kali(4,6)}')


pangkat = lambda num,pangkat: num**pangkat
print(f'hasil lambda pangkat = {pangkat(4,4)}')

print('\n')

## kegunaannya apa?

# sorting untuk list abjad
list_data = ['aku', 'kamu', 'dia', 'me']
list_data.sort()
print(f'sorted list = {list_data}')

# sorting berdasarkan panjang 

def panjang_nama(nama):
    return len(nama)

list_data.sort(key = panjang_nama)
print(f'sorted list by panjang = {list_data}')

# sort pakai lambda
list_data = ['aku', 'kamu', 'dia', 'me']

list_data.sort(key = lambda nama:len(nama))
print(f'sorted list by lambda = {list_data}')

print('\n')

# filter
data_angka = [
    1,2,3,4,5,6,7,8,9,10,11,12,12,14,15,16,17,18,19,20
    ]

print(f'data angka = {data_angka}\n')
def kurang_dari_lima(angka):
     return angka < 5

data_angka_baru_biasa = list(
    filter(
        kurang_dari_lima, data_angka
        )
    )
print(f'angka kurang dari 5 = {data_angka_baru_biasa}')

# menggunakan lamda 
data_angka_baru_lamda = list(
    filter(
         lambda angka: angka < 7, data_angka
         )
    )
print(f'angka kurang dari 7 = {data_angka_baru_lamda}')

print('\n')

# kasus genap 

data_genap = list(
    filter( 
        lambda angka: angka%2==0, data_angka
        )
    )
print(f'data angka genap = {data_genap}')

# kasus ganjil 

data_ganjil = list(
    filter(
        lambda angka: angka%2!=0, data_angka
    )
)
print(f'data angka ganjil = {data_ganjil}')

# kelipatan 3

data_3 = list(
    filter(
        lambda angka: angka%3==0, data_angka
    )
)
print(f'data angka kelipatan 3 = {data_3}')

