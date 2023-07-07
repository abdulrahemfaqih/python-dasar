'''by : ARF'''
# format string 
import os
os.system('cls')
# contoh generic 
# string 
nama = 'abdul rahem faqih'
str = 'hello nama saya' + nama
print(str)
formatStr = f'hello nama saya {nama}'
print(formatStr)

# boolean 
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka     
angka = 1234.8
angka_biasa = f'angka = {angka}'
print(angka_biasa)

# angka ribuan, jutaan, dll
angka = 15000
format_str = f'ribuan =  {angka:,}'
print(format_str)
angka = 40209352836523869
formatstr = f'triluwun =  {angka :,} ' 
print(formatstr)

# angka desimal 
angka = 1984245.283500
formatstr = f'desimal = {angka :.5f}' 
# hanya mengambil 4 angka di belakang koma
print(formatstr)

# menampilkan leading zero 
angka = 12345.789
leadingZero = f'desimal = {angka:014.4f}'
# bisa menambah 0 di di leadingnya
print(leadingZero)

# menampilkan tanda - dan +
angkaMinus = -293865.1986325
angkaPlus = 9182365
format_minus = f'minus = {angkaMinus :+.3f}'
format_plus = f'plus = {angkaPlus :+}'
print(format_minus)
print(format_plus)

# format persen
persentase = 0.56
format_persen = f'persen = {persentase:.2%}' 
    # menampilkan persen
print(format_persen)

# operasi aritmatika di dalam {}(place holder)
harga = 2000
jumlah = 7
format_str = f'hartot = Rp.{harga*jumlah:,}'
print(format_str)

# format angka lain seperti : binary, octal, hexadesimal

angka = 1234
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)