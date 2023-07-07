from multiprocessing.sharedctypes import Value
import os
os.system('cls')

value_1 = int(input('masukkan nilai pertama : '))
value_2 = int(input('masukkan nilai kedua : '))

if value_1 > value_2:
    # program menukar variabel value_1 dan value_2
    var_bantu = value_1
    value_1 = value_2
    value_2 = var_bantu

    print(f'nilai pertama : {value_1}')
    print(f'nilai kedua : {value_2}')



