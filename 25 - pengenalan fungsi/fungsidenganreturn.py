import os
os.system('cls')
# FUNGSI DENGAN KEMBALIAN (RETURN VALUE)

# TEMPLATE FUNGWI DENGAN KEMBALIAN 

'''
def nama_fungsi(argument):
  badan fungsi
  return output
'''

# FUNGSI KUADRAT

def kuadrat(input_angka):
  '''fungsi kiadrat'''
  return input_angka**2

x = kuadrat(100)
y = kuadrat(5)

print(f'100 kuadrat = {x}\n5 kuadrat = {y}')
print(f'x + y = {x + y}')

# FUNGSI TAMBAH 

def tambah(angka1, angka2):
  return angka1 + angka2

z = tambah(1,3)
c = tambah(100,5)
print(f'1 + 100 = {z + c}\n') 

# OPERASI MATEMATIKA - fungsi dengan return banyak 

def operasi_aritmatika(angka1, angka2):
  tambah = angka1 + angka2
  kurang = angka1 - angka2
  kali = angka1 * angka2
  bagi = angka1 / angka2

  return tambah,kurang,kali,bagi 

f,h,i,j = operasi_aritmatika(100,32)
print(f'diket angka 100 dan 32\n')

print(f'hasil tambah = {f}')
print(f'hasil kurang = {h}')
print(f'hasil kali   = {i}')
print(f'hasil bagi   = {j}')

def tambah(a1,a2):
  hasil = a1*a2
  return hasil 

print(tambah(1,2))












































