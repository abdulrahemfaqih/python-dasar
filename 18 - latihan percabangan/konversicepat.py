'''
  buatlah codingan dari konversi kecepatan m/s ke km/jam ataupun sebeliknya, menggunakan input user 
'''

print('\nopsi : M/S - KM/H , KM/H - M/S \n')
opsi = input('masukkan opsi di atas :')
input_Angka = float(input('masukkan angka yang di konversi = '))

if opsi == 'M/S - KM/H':
  hasil = input_Angka/1000
  print(f' {hasil} kM/H')
elif opsi =='KM/H - M/S':
  hasil = input_Angka*1000
  print(f'{hasil} M/S')
else :
  print('input tidak dikenali')

  