import os
os.system('cls')

# 1. 

# price1 = '$1.45'
# price2 = '$2.38'

# print(f'{price1}\n{price2}')

# 2. 

# harga_awal, diskon = (
#     int(input('masukkan harga barang : ')),
#     int(input('masukkan harga diskon : '))
# )

# harga_diskon = harga_awal*(diskon/100)
# harga_setelah_diskon = harga_awal - harga_diskon
# print(f'total bayar Rp. {harga_setelah_diskon}')

# 3. 

celcius = int(input('masukkan suhu celcius : '))

fahrenheit = (9/5 * celcius) + 32
kelvin = celcius + 273

print(f'suhu dalam derajat fahrenheit = {fahrenheit}')
print(f'suhu dalam derajat kelvin = {kelvin}')

