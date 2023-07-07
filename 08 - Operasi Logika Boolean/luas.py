print('NAMA  : ABDUL RAHEM FAQIH')
print('NIM   : 2200411100029')
print('KELAS : IF 1A')

''' 1. MENGHITUNG LUAS PERSEGI PANJANG
    2. MENGHITUNG LUAS PERSEGI
    3. MENGHITUNG LUAS SEGITIGA
    4. MENGHITUNG LUAS LINGKARAN
'''
# 1.
print('\n1. MENGHITUNG LUAS PERSEGI PANJANG')
P = float(input('masukkan panjang sisi:'))
l = float(input('masukkan lebar sisi  :'))
luas = P*l
print('luas =', luas)

#2.
print('\n2. MENGHITUNG LUAS PERSEGI')
s = float(input('masukkan panjang sisi:'))
luas = s*s
print('luas =', luas)

#3.
print('\n3. MENGHITUNG LUAS SEGITIGA ')
a = float(input('masukkan nilai alas  :'))
t = float(input('masukkan nilai tinggi:'))
luas = 0.5*a*t
print('luas =', luas)

#4.
print('\n4. MENGHITUNG LUAS LINGKARAN')
r = float(input('masukkan nlai jari - jari :'))
phi       = 3.14
luas      = phi*r*r
print('luas =', luas)    
