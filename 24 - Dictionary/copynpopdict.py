# COPY AND POP DICTIONARY

# COPY DICTIONARY
import os
os.system('cls')
buah_buah = {
  'mg' : 'mangga',
  'ps' : 'pisang', 
  'ag' : 'anggur',
  'ap' : 'apel',
  'kl' : 'kelengkeng',
  'ms' : 'manggis',
  'kp' : 'kelapa',
  'py' : 'pepaya'            
}

fruits = buah_buah.copy()
fruits['mg'] = 'manggis'

print(f'\nbuah-buahan : {buah_buah}\n')
print(f'fruits      : {fruits}\n')

# POP DICTIONARY --> membuat variabel baru dari data dictionarynya sekaligus menghilangkan data di dalam dictionary tersebut

fruits.pop('mg')

print(f'fruits = {fruits}\n')

# POP ITEM --> mengambil data terakhir

dataTerakhir = fruits.popitem()
print(f'data terakhir = {dataTerakhir}')

