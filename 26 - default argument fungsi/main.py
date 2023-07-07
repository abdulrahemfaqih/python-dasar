import os
os.system('cls')

'''DEFAULT ARGUMENT'''

def say_hello(nama = 'kamu'):
  print(f'halo {nama}')

say_hello('aku')
say_hello()

def sapa_menyapa(nama,pesan = 'apa kabar lu asw?!'):
  '''fungsi dengan satu input biasa, dan satu dengan default argument'''
  print(f'kepada {nama}, {pesan}')

sapa_menyapa('anonim', 'bagemana kaber lu?')
sapa_menyapa('koreng')

def menghitung_pangkat(angka,pangkat):
  hasil = angka**pangkat
  return hasil

print(menghitung_pangkat(2,7))

def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
  hasil = input1 + input2 + input3 + input4
  return hasil 


print(fungsi())
print(fungsi(input1 = 13))
print(fungsi(1,2,3,4))




