import os
os.system('cls')

'''fungsi pangkat'''
tanya = 'y'
while True:
  def pangkat():
    angka = int(input('masukkan angka = '))
    pangkat = int(input('masukkan pangkat = '))
    if pangkat == 1:
      print(f'{angka}^{pangkat} = {angka}')
    else:
      print(f'{angka}^{pangkat} = {angka**pangkat}')


  pangkat()
  tanya = input('mau lanjut berhitung? (y/n) = ')
  if tanya == 'n':
    print('')
    break


  


    
    




