import os
os.system('cls')



'''Key Words *args (**kwargs)'''

def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f'nama saya {nama}, tinngi saya {tinggi}, berat saya {berat}')

fungsi('farish',176,56)

def fungsi(**kwargs):
    '''fungsi dengan **kwargs'''
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f'nama saya {nama}, tinngi saya {tinggi}, berat saya {berat}')

fungsi(nama='farish', tinggi=176, berat=56) # hasilnya dict

# study kasus

def math(*args, **kwargs):
    if kwargs['option'] =='tambah':
        output = 0
        for angka in args:
            output += angka

    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka

    elif kwargs['option'] == 'bagi': 
        output = 1
        for angka in args:
            output /= angka

    elif kwargs['option'] == 'pangkat':
        output = 1
        for angka in args:
            output **= angka

    return output


hasil = math(1,2,3,4,5, option = 'tambah')
print(f'hasil tambah {hasil}')

hasil = math(1,2,3,4,5, option = 'kali')
print(f'hasil kali {hasil}')

hasil = math(1,2,3,4, option = 'bagi')
print(f'hasil bagi = {hasil}')

hasil = math(1,2,3,4,5, option = 'pangkat')
print(f'hasil pangkat = {hasil}')
