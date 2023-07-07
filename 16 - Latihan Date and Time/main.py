# date and time (latihan)
import os
os.system('cls')
import datetime as dt
# date kita import sebagai dt

# hariIni = dt.date.today()
# print(hariIni)
# print(f'hari ini adalah hari : {hariIni:%A}')

# tanggalLahir = dt.date(2003,12,26)
# print(tanggalLahir)
# print(f'hari tanggal lahir ku : {tanggalLahir:%A}')
print('silahkan masukkan TTL\n')
tanggal,bulan,tahun = (
    int(input('input tanggal ')),
    int(input('input bulan \t: ')),
    int(input('input tahun \t: ')),
    ) 
    
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f'TTL anda \t: {tanggal_lahir}')
print(f'hari \t\t: {tanggal_lahir :%A}')

hari_ini = dt.date.today()
print(f'hari ini \t: {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365 ) // 30
print(f'umurmu dalah hari  : {umur_hari}')
print(f'umurmu dalam bulan : {umur_bulan_sisa} bulan ')
print(f'umurmu dalam tahun : {umur_tahun} tahun ')
