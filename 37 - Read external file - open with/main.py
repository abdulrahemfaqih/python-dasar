import os
os.system('cls')
print(f'{5*"-"} membaca file txt {5*"-"}')

file = open('data.txt', mode="r")

print(f'status read = {file.readable()}')
print(f'status write = {file.writable()}')

# baca seluruh file
# print(file.read()) 


# baca perbaris
print(file.readline(), end= "") # baca baris pertama
print(file.readline(), end= "") # baca baris kedua
print(file.readline()) # baca baris ketiga

# baca sebagai list
# print(file.readlines())

# check file is closed?
print(f'apakah dile sudah di closed : {file.closed}')

# menutup file
file.close()
print(f'apakah dile sudah di closed : {file.closed}')


## salah satu teknik membuka file di python
print(f'\n{5*"-"} membaca file txt dengan with{5*"-"}')

with open('data.txt', mode='r') as file :
  content = file.read()
  print(content)
  print(f'apakah dile sudah di closed : {file.closed}')
  # file masih terbuka jika masih dalam with
  
print(f'apakah dile sudah di closed : {file.closed}') # file otomatis ketutup jika diluar with
  




