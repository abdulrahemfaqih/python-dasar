import os
os.system('cls')
print('buatlah program perulangan "kamu nanya?", jika angka mencapai batas continue yang ditetukan oleh user,sehingga mengeluarkan ouput "iya aku nanya" mengeluarkan ouput ("iya aku nanya"),  ouput harus sesuai contoh\n')

awal = int(input('masukkan angka awal = '))
batas = int(input('masukkan angka continue = '))
akhir = int(input('masukkan batas perulangan = '))



# perulangan while

# x = 0
# while x < akhir:
#   x += 1
#   if x == batas:
#     print('iya aku nanya - ',x)
#     continue
#   print('kamu nanya? - ',x)
# print('\nkamu bertanya-tanya bagaimana caranya?, semangat ya\n')

# perulangan for

for i in range(awal, akhir + 1):
  if i == batas:
    print(f'iya aku nanya - {i}')
    continue
  print(f'kamu nanya? - {i}')



 













