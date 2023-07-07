# break

angka = 0

while angka < 5:
  angka += 1
  print(f'angka sekarang --> {angka}')

  if angka ==3:
    print('halo')
    break 
    # fungsinya --> tidak mengeksekusi angka setelah tiga karena sudah di hentikan 

  print('hai')

print('selesai\n')

# program mengitung 
angka = 0
data  = int(input('hitung sampai = '))


while True:
  angka += 1
  print(f'angka = {angka}')

  if angka == data:
    break
  
print('sudah')







  
