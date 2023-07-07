# exception akan terjadi saat program mengalami eror saat runtime 

# contoh sederhana utuk menangkap exception 
import os
os.system('cls')



# input_user = int(input('maukkan angka: '))
# hasil = 'tidal terdefinisi'

# try :
#   hasil = 10/input_user
# except:
#   print('input tidak boleh 0')

# print(f'hasil = {hasil}')


## contoh 2

while True:
  # os.system('cls')
  angka = int(input('masukkan angka = '))
  angka_p = int(input('masukkan angka pembagi: '))

  try:
    hasil = 10/angka_p
    print(f'10/{angka_p} = {hasil}')
    tanya = input('mau lanjut (y/n)?: ' )
    
    if tanya == 'n':
      break

  except:
    print(f'10/{angka_p} = tidak terdefinisi')

print('program selesai')

# angka = int(input('masukkan angka = '))
# angka_p = int(input('masukkan angka pembagi = '))

# hasil = angka/angka_p
# print(hasil)

  