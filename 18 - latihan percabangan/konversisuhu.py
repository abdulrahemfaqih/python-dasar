'''
  konversi suhu c celcius ke fahrenheit, celcius ke kelvin, celcius ke reamur menggunakan input user 
'''

print(20*'=')
print('konversi suhu')
print(20*'=' + '\n')

celcius = float(input('masukkan suhu dalam celcius = '))
opsi = input('silahkan pilih \nopsi(C to F, C to K, C to R) : ')

if opsi =='C to F':
  hasil = (9/5) * celcius + 32
  print(f'suhu dalam Fahrenheit = {hasil} ')
elif opsi =='C to K':
  hasil = celcius + 273
  print(f'suhu dalam Kelvin = {hasil}')
elif opsi == 'C to R':
  hasil = (4/5) * celcius 
  print(f'suhu dalam Reamur = {hasil}')
else:
  print('opsi tidak di kenali')
print('Terimakasih')


