import os
os.system('cls')

print('buatlah program mengakhiri pemasukan data angka, jika user memasukkan data, misal 0, maka program akan berhenti dan menghitung rata-ratanya\n')


data = int(input('masukkan angka = '))
angka = 0
total = 0
while data != 0:
  angka += 1
  total += data
  data = int(input('masukkan angka = '))
mean = total/angka
print(f'\nmean = {mean}\n')















  