import os
os.system('cls')

'''program menghitung hurf besar dan kecil pada string'''

kalimat = input('masukkan kalimat = ')

jum_huruf_besar = 0
jum_huruf_kecil = 0

for i in kalimat:
  if i.isupper():
    jum_huruf_besar += 1
  else:
    jum_huruf_kecil += 1

print(f'huruf besar = {jum_huruf_besar}')
print(f'huruf kecil = {jum_huruf_kecil}')

print()


