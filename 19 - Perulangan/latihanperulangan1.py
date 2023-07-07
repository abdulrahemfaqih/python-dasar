import os
os.system('cls')


angka = int(input('masukkan angka = '))

if angka > 1:
    for i in range(2,angka):
        if (angka%1) == 0:
            print(f'{angka} bukan bilangan prima')
            break
        else:
            print(f'{angka} bilangan prima')


else:
    print(f'{angka} bukan bilangan prima')
    5
