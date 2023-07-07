'''Latihan Fungsi''' 
import os
# program menghitung keliling dan luas persegi panjang  

def header():
  '''fungsi header'''
  os.system('cls')
  print(f'\n{"PROGRAM MENGHITUNG LUAS" : ^40}')
  print(f'{"DAN KELILING PERSEGI PANJANG" : ^40}\n')
  print(f'{"-"*40 : ^40}')

def input_user():
  '''fungsi mengambil input user'''
  print('\nmenggunakan satuan CM')
  lebar = float(input('masukkan lebar sisi = '))
  panjang = float(input('masukkan panjang sisi = '))

  return lebar, panjang 

def hitung_luas(lebar,panjang):
  '''fungsi luas'''
  hasil = panjang*lebar
  return hasil

def hitung_keliling(lebar,panjang):
  '''fungsi keliling'''
  hasil = 2*(panjang+lebar)
  return hasil

def display(message, value):
  '''fungsi display'''
  print(f'\nhasil perhitungan {message} = {value} CM')
def selesai():
  print('\nenakkan gausa ngitung wkwkw\n')

# program utama

while True:
  header()
  opsi = input('ketik 1 untuk menghitung luas\nketik 2 untuk menhitung keliling \n= ')

  if opsi == '1':
    lebar,panjang = input_user()
    luas = hitung_luas(lebar,panjang)
    display('luas = ', luas)
  
  elif opsi == '2':
    lebar,panjang = input_user()
    keliling = hitung_keliling(lebar,panjang)
    display('keliling ', keliling)
  else:
    print('\nsalah memasukkan opsi, ketik opsi (1/2) untuk menghitung')

  
  lanjut_tidak = input('\napakah ingin lanjut menghitung(y/n)? : ')
  if lanjut_tidak == 'n':
    break

selesai()