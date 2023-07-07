# # latihan logika dan komparasi
# # membuat gabungan area rentang dari angka
# # ++++++7-----------17++++++

# inputUser = float(input("masukkan angka yang nilainya\n< 7 atau > 17 ="))

# # +++++3------------------
# # memeriksa angka <7
# isKurangDari = (inputUser < 7)
# print(" Kurang dari 7 =", isKurangDari)

# # ------------10++++++++++
# # memeriksa angka >17
# isLebihDari = (inputUser > 17)
# print(" Lebih dari 17 =", isLebihDari)

# # bagaimana juka biar bisa gabung = kita gunakan or
# # +++++7--------17++++++

# isCorrect = isKurangDari or isLebihDari
# print("Angka yang anda masukkan :", isCorrect)

# '''mengapa menghasilkan true? karena angka 
# yang dimasukkan memeniho rentang itu '''

# # irisan 
# # ------7++++++=17------
# inputUser = float(input("masukkan angka yang nilai nya\n > 7 dan < 17 =" ))

# #-----7++++
# isLebihDari = inputUser > 7
# print("Lebih Dari 7 =", isLebihDari)

# # +++++17----
# IsKurangDari = inputUser < 17
# print("34 Kurang Dari 17 = ", isKurangDari)

# # kita iriskan dari kedua persamaan tadi
# isCorrect = isLebihDari and isKurangDari
# print("angka yang anda masukkan ;", isCorrect)


# pr
# 1. ----0+++++5-----8++++++11-----

# inputUser = float(input("masukkan angka yang bernilai\n <0 dan <5 \n atau >8 dan <11 ="))

# angka1 = inputUser > 0
# angka2 = inputUser < 5
# angka3 = inputUser > 8
# angka4 = inputUser < 11






# or 
p = True
q = False
hasil = p or q
print(f'{p} or {q} = {hasil}')

p = False
q = False
hasil = p or q 
print(f'{p} or {q} = {hasil}')

# contoh penggunaan menentukan area rentang
# ++++10------17+++++, memeriksa angka < 10 atau > 17
angka = int(input('masukkan angka\nyang nilainya < 10 atau > 17 = '))
kurang_dari = angka < 10
print(f'< 10 = {kurang_dari}')
lebih_dari = angka > 17
print(f'> 17 = {lebih_dari}')
hasil = kurang_dari or lebih_dari
print(f'angka yang anda inputkan = {hasil}')





# coba bikin menggunakan 'and' membuat irisan 

# -------10+++++++17------



# not

p = True
q = not p
print(f'nilai p = {p}')
print(f'nilai p setelah di not = {q}')