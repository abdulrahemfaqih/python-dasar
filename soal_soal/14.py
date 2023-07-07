import os
os.system('cls')

'''membuat program mencari kata atau huruf'''

kalimat = input('masukkan kalimat = ')
find = input('masukkan apa yang mau dicari = ')

print(f'posisi {find} pada {kalimat} = {kalimat.find(find)}')