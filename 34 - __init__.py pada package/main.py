import os

os.system('cls')

import sains


hasil_tambah = sains.mtk.tambah(12,12,34,56)

print(
    f'hasil tambah = {hasil_tambah}'
)

hasil_kali = sains.mtk.kali(12,12,34,56)

print(
    f'hasil kali = {hasil_kali}'
)

c_to_k = sains.kimia.kelvin(12)
print(
    f'12 celcius = {c_to_k} kelvin'
)

pangkat = sains.pangkat(2,100)

print(
    f'2 pangkat 100 = {pangkat}'
)