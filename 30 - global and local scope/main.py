# GLOBAL AND LOCAL SCOPE

import os
os.system('cls')

## Variabel global scope
nama_global = 'faqih'

# akses vaiabel global dalam fungdi
def nama():
    print(f'halo {nama_global}')
nama()


# akses variabel global dalam loop
for i in range(1,5+1):
    print(f'loop {i} - {nama_global}')

# percabangan

if True:
    print(f'menampilkan {nama_global}')

## Variabel Lokal Scope

def nama2():
    nama_lokal = 'faqih' # variabel lokal scope 
    return nama_lokal

print(nama2())

## contoh penggunaan 1 : akses variabel

def name():
    print(f'nama kamu siapa sih, nama aku adalah {nama_kamu}')

nama_kamu = 'faqih'
name()

# contoh penggunaan 2 : merubah variabel global 


angka = 1
# merubah nya menggunalan 'global scope'










    