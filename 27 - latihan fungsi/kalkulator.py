import os
def header():
    os.system('cls')
    print(f'\n{"KALKULATOR SEDERHANA" : ^40}')
    print(f'{"-"*40 : ^40}')

def input_user():
    angka_pertama = int(input('masukkan angka pertama = '))
    angka_kedua = int(input('masukkan angka kedua = '))
    return angka_pertama, angka_kedua

def penjumlahan(angka_pertama, angka_kedua):
    hasil = angka_pertama + angka_kedua
    return hasil

def pengurangan(angka_pertama, angka_kedua):
    hasil = angka_pertama + angka_kedua
    return hasil

def perkalian(angka_pertama, angka_kedua):
    hasil = angka_pertama + angka_kedua
    return hasil

def pembagian(angka_pertama, angka_kedua):
    hasil = angka_pertama + angka_kedua
    return hasil

def display(message, value):
    print(f'hasil perhitungan {message} = {value}')

def selesai():
    print('program selesai')

while True :
    header()

    opsi = input(
        (
            'ketik 1 untuk penjumlahan\nketik 2 untuk pengurangan\nketik 3 untuk perkalian\nketik 4 untuk pembagian \n = '
        )
    )

    if opsi == '1':
        angka_pertama, angka_kedua = input_user()
        hasil = penjumlahan(angka_pertama, angka_kedua)
        display(' = ', hasil)
    
    elif opsi == '2':
        angka_pertama, angka_kedua = input_user()
        hasil = pengurangan(angka_pertama, angka_kedua)
        display(' = ', hasil)
    
    elif opsi == '3':
        angka_pertama, angka_kedua = input_user()
        hasil = perkalian(angka_pertama, angka_kedua)
        display(' = ', hasil)
    
    elif opsi == '4':
        angka_pertama, angka_kedua = input_user()
        hasil = pembagian(angka_pertama, angka_kedua)
        display(' = ', hasil)

    lanjut_tidak = input('mau lanjut mengitung atau tidak (y/n) = ')

    if lanjut_tidak == 'n':
        break
    
selesai()
    






