# operator dictionary
import os
os.system('cls')
data_dict = {
  'key' : 'value',
  'nmr' : 100,
  'dt'  : 'halo'
}
print(f'\ndata_dict asli = {data_dict}\n')

# panjang dictionary
lendict = len(data_dict)
print(f'jumlah data = {lendict}\n')

# mengecek key exist(ada) atau tidak
key = 'dt'
key1 = 'sbr' 
checkkey = key in data_dict
checkkey1 = key1 in data_dict
print(f'apakah {key} ada di dalam data_dict : {checkkey}')
print(f'apakah {key1} ada di dalam data_dict : {checkkey1}\n')

# mengakses value (read) dengan get 
print(data_dict['dt'])
print(data_dict.get('dt'))
print(data_dict.get('smr')) # --> akan menghasilkan none karena tidak ada key yang bernama smr

#  mengupdate data
data_dict['nmr'] = 900
print(f'\ndata_dict setelah diupdate =\n{data_dict}\n')
data_dict['sbr'] = 'subroto'
print(f'data_dict setelah ditambah =\n{data_dict}\n')

# menggunakan update --> jika datanya tidak ada tinggal add aja, lain halnya jika menggunakan yang di atas 
data_dict.update({'nmr': 100})
print(f'data_dict diupdate lagi =\n{data_dict}\n')
data_dict.update({'alm' : 'almarhum'})
print(f'data_dict setelah ditambah lagi =\n{data_dict}\n')

# mendelete data pada dictionary
del data_dict['nmr']
print(f'data_dict paling update = {data_dict}\n')




