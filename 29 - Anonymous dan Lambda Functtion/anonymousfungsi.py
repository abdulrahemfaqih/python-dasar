import os
os.system('cls')

'''Anonymous Function'''
# currying <-- Haskell Curry

# fungsi biasa

def pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

data_hasil = pangkat(2,10)
print(f'2**10 = {data_hasil}')

# dengan currying

def pangkat(n):
    return lambda angka:angka**n

print(f'4**5 = {pangkat(5)(4)}')
