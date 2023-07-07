import os
os.system('cls')
# operasi dan manipulasi string
print('\n==OPERASI MANIPULASI STRING==')
# 1. menyambung string ( concate)
print('\n-----mennggabungkan string')
nama_depan = "abdul"
nama_tengah = "rahem"
nama_belakang = 'faqih'
nama_lengkap = nama_depan +" "+ nama_tengah +" "+ nama_belakang
print(nama_lengkap)

# 2. menghitung panjang  string 
print('\n----menghitung panjang string')
panjang = len(nama_lengkap)
print('panjang dari ' + nama_lengkap + " = " + str(panjang) )

#3. operator untuk string
# mengecek apakah ada komponen char/string di string
print('\n----statusing string')
d = 'd'
status = d in nama_lengkap
print(status)
z = 'z'
status = z in nama_lengkap
print(status)

#mengulang string
print('\n---mengulang string')
print('kwkwkwk'*10)

# indexing = megambil data dari string
print('\n---indexing')
print(nama_lengkap)
print('index ke-0 :'+ nama_lengkap[0] )
print('index ke-7 :' + nama_lengkap[7])
print('index ke -(-1) :' + nama_lengkap[-1])
print('index ke-(-2)  :' + nama_lengkap[-2])
print('index ke-[0:4] :' + nama_lengkap[0:5]) # di python mesti mengurangi 1 huruf, jadi harus melebihkan 1 huruf
print('index ke-[6:10]:' + nama_lengkap[6:11]) 
print('index ke-[12:16] :' + nama_lengkap[12:17]) 
print('index ke-[0,6,12]:' + nama_lengkap[0:13:6]) 

#menentukan item paling kecil dan paling besar
print('\n---item paling kecil dan besar')
print('huruf/item paling kecil :' + min(nama_lengkap)) # paling kecil adalah spasi wkwk
print('huruf/item paling besar :' + max(nama_lengkap))

# 4. OPERATOR DALAM BENTUK METHOD
print('\n===operator dalam bentuk method')
data = "jangan panggil aku shiva"
jumlah = data.count('a')
print('\njumlah  huruf a pada ' + data + ' = ' + str(jumlah))
jumlah = data.count('z')

## merubah case dari string

# merubah semua ke upper case dan lower case
print('merubah case dari string')
salam = 'Cok! asw teko nandi'
print('\nnormal =' + salam)
salam = salam.upper()
print('upper  =' + salam)
salam = salam.lower()
print('lower  =' + salam)

## pengecekan dengan isX methods

# contoh untuk pengecekan lower case
print('\n')
salam = "Tod"
apakah_lower = salam.islower()
print(salam + 'is lower =' + str(apakah_lower))

# contoh pengecekan upper case
apakah_upper = salam.isupper() # hasilnya bool maka dari itu di tambah str
print(salam +'is upper = ' + str(apakah_upper))

# isalpha() ---> untuk mengecek semuanya huruf
# isalnum() ---> untuk mengecek huruf dan angka
# isdecimal() ---> untuk mengecek semuanya angka
# isspace()  ----> tab, newline , spasi
# istittle ---> semua kata dimuali huruf besar
print('\n')
password = 'Abdul Rahem Faqih 99'
cekpassword = password.isalnum()
print(password + 'is alnum =' + str(cekpassword))
apakah_alpha = password.isalpha()
print(password +'is alpha =' + str(apakah_alpha))
apakah_decimal = password.isdecimal()
print(password + ' is decimal =' + str(apakah_decimal))
apakah_space = password.isspace()
print(password + ' is space =' + str(apakah_space))
apakah_tittle = password.istitle()
print(password + ' is tittle =' + str(apakah_tittle))

# ngecek komponen startswith dan endswith 
print('\n')
cek_start = " shiva abdul manab".startswith('p')# karena di awali dengan spasi
print('start ='+ str(cek_start))
cek_start = "olovia abdul manabbb".endswith('abdul') 
print( 'end =' + str(cek_start))

# penggabungan komponen join() dan split()
print('\n')
judul = ['aku','dan','kau']
penggabungan = '-'.join(judul)
print(penggabungan)

penggabungan = ', '.join(judul)
print(penggabungan)

# alokasi karakter rjust(), ljust(), center
nama = 'abdul rahem faqih'.rjust(20)
print(nama)
nama = 'aku siapa kamu'.ljust(20)
print(nama)
nama = 'abdul rahem faqih'.center(50)
print(nama)

A = 3
print(f'a {3}.'.rjust(100))
task = [1]

print(f'Proses {task[0]} selesai'.rjust(40))










