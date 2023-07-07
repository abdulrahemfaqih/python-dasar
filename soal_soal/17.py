import os
os.system('cls')

kumpulan_angka = input('masukkan bilangan = ')

if not kumpulan_angka.isdigit():
  print('string harus berupa bilangan')

else: 
  jumlah = 0
  for indeks in kumpulan_angka:
    jumlah = jumlah + int(indeks)
    print(indeks)

  print('-----+')
  print(jumlah,'\n')



  
