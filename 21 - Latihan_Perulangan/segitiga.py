 # LATIHAN PERULANGAN 


tinggi = 15

# 1. Menggunakan For

# dummy variable

# print('------ AWAL FOR ------\n')
# count = 1
# for i in range(tinggi):
#   print('-'*count)
#   count += 1

# print('\n------ AKHIR FOR -----\n')

# 2. Menggunakan While 

print('------ AWAL WHILE ------\n')
count = 0
panjang = int(input('masukkan panjang segitiga : '))

while True:
  print(f'-'*count)
  count += 1

  if count == panjang :
    break


print('\n----- AKHIR WHILE ------\n')


# 3. Hanya Bilangan Ganil 
count = 0
panjang = int(input('masukkan panjang segitiga : '))

while True:

  if count % 2 : 
    # akan print jika ganil 
    print('-'*count)
    count += 1
  
  else :
    count += 1
    continue
 

  if count == panjang :
    break



