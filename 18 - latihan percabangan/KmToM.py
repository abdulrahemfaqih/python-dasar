

print('opsi (Dolar to Rupiah, Rupiah to dolar) :')
opsi = input('pilih konversi :')
uang = float(input('masukkan angka :'))

if opsi =='Dolar to rupiah':
  hasil = uang*15000
  print(f' {hasil} dolar ')
elif opsi == 'Rupiah to Dolar':
  hasil = uang/15000
  print(f' {hasil} rupiah ')
else :
  print('input tidak dikenali ')
print('terimakasih telah menggunakan jasa')





# inputanAngka = float(input('masukkan angka yang mau di konversi = '))
# opsi = input('silahkan pilih opsi (M to KM, KM to M)  :')

# if opsi == 'KM to M':
#   hasil = inputanAngka*1000
#   print(f' {hasil } M')
# if opsi == 'M to KM ':
#   hasil = inputanAngka/1000
#   print(f' {hasil} M ')
# else :
#   print('opsi tidak di kenali ')

# print('terimkasih telah menggunakan jasa')



