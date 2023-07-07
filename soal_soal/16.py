import os
os.system('cls')

huruf_vokal = 'aiueoAIUEO'

kalimat = input('masukkan kalimat = ')

hasil = ''

for i in kalimat:
  vokal = False

  #mengecek huruf vokalkah?
  for j in huruf_vokal:
    if i == j:
      vokal = True
      break

  if not vokal:
    hasil += i

print(f'setelah huruf vokal dihapus = {hasil}\n')








 

  