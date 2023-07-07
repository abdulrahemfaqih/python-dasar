'''
  BUAT LAH PROGRAM KONVERSI PANJANG 
  JIKA USER MENGINPUT 1 MAKA AKAN MENGHITUNG KM TO M
  JIKA USER MENGINPUT 2 MAKA AKAN MENGHITUNG M TO KM
'''
print('1. KM to M')
print('2. M to KM')

opsi1 = float(input('silahkan masukkan opsi 1 ; '))
if opsi1 == 1:
  a = float(input('masukkan angka : '))
  print(a*1000, "M")
elif opsi1 == 2:
  b = float(input('masukkan angka : '))
  print(b/1000, "KM")
else :
  print ("input mu ga sesuai cok")

print('\nhahah')

