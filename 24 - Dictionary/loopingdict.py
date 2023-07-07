import os
os.system('cls')


nama_buah = {
  'mg' : 'mangga',
  'ps' : 'pisang', 
  'ag' : 'anggur',
  'ap' : 'apel',
  'kl' : 'kelengkeng',
  'ms' : 'manggis',
  'kp' : 'kelapa',
  'py' : 'pepaya'            
}

# looping 1 (yang keluar adalah KEY nya)
print('\n')
for buah in nama_buah :
  print(buah)
print('\n')

# operator untuk mengambil item / iterables
key = nama_buah.keys()
print(key)


for key in nama_buah.keys():
  print(key)
print('\n')

# value = nama_buah.values()
# print(value)

# for value in nama_buah.values():
#   print(value)
# print('\n')

items = nama_buah.items()
print(items)

for item in nama_buah.items():
  print(item)

for key,value in nama_buah.items():
  print(f'key = {key}, value = {value}')