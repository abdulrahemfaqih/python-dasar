import os
os.system('cls')

# __main__ adalah top level code environment

# __name__ = __main__ akan terjadi jika ada diprogram uatam

## __name__ pada file program utama
print(f'nilai __name__ pada program main.py = "{__name__}"')

## __name__ pada file eksternal
import fungsi

## contoh penggunaan __main__

# deklarasi

def fungsi_kali(a,b):
  return a*b

# fungsi utama 

if __name__ == '__main__':
  angka1 = 100
  angka2 = 10
  hasil = fungsi_kali(angka1,angka2)
  print(f'hasil kali = {hasil}')

## import package
import package



