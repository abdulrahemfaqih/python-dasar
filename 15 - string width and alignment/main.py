import os
os.system('cls')
print(5*'=' + 'data string' + 5*'=')
data_nama = 'abdul rahem faqih'
data_umur = 19
data_tinggi = 168.2
data_ukuran_baju = 'L'
data_ukuran_sepatu = 41

# data_string = f'nama = {data_nama} umur = {data_umur} tinggi = {data_tinggi} ukuran baju = {data_ukuran_baju} nomor sepatu = {data_ukuran_sepatu}'
# print(data_string)

# string multiline ( menggunakan enter atau newline (\n))
data_string = f'nama = {data_nama} \numur = {data_umur} \ntinggi = {data_tinggi} \nukuran baju = {data_ukuran_baju} \nnomor sepatu = {data_ukuran_sepatu}'

print(data_string)

# string multiline ( tanda kutip 3)

data_string = f'''nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
baju   = {data_ukuran_baju}
sepatu = {data_ukuran_sepatu}
'''
print('\n',5*'-'+ 'menggunakan tanda kutip 3' + 5*'-')
print(data_string)

# mengatur lebar 
data_nama = 'faqih'
data_string = f'''nama   = {data_nama :>8}
umur   = {data_umur :>5}
tinggi = {data_tinggi :>8}
baju   = {data_ukuran_baju :>4}
sepatu = {data_ukuran_sepatu :>5}
'''
print('\n',5*'-'+ 'mengatur lebar' + 5*'-')
print(data_string) 