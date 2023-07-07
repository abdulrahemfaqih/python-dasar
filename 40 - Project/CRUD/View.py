from . import Operasi





def update_console():
  print('silahkan update cuy')






def create_console():
  print(f'\n{"="*75}')
  print(f'{"silahkan tambah data anime" : ^75}')
  print(f'{"-"*75}')
  judul = input('Judul\t: ')
  rate = input('Rating\t: ')

  while True:
    try:
      tahun = input('Tahun\t: ')
      if len(tahun) == 4:
        break
      else:
        print('Tahun harus berupa angka, silahkan inputkan kembali (yyyy)')

      
    except:
      print('Tahun harus berupa angka, silahkan inputkan kembali (yyyy)')

  
  Operasi.create(tahun,judul,rate)
  print('\nberikut adalah data baru anda')
  Operasi.read()




def read_console():
  data_file = Operasi.read()

  index = 'No'
  judul = 'Judul'
  rate = 'Rate'
  tahun = 'tahun'

  '''header'''
  print(f'\n{"="*75}')
  print(f'{index:4} | {judul:40} | {rate:15} | {tahun:5}')
  print(f'{"-"*75}')

  '''data'''

  for index, data in enumerate(data_file):
    data_break = data.split(',')
  

    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    rate = data_break[3]
    tahun = data_break[4]
    print(f'{index + 1 :4} | {judul:.40} | {rate:.15} | {tahun:4}', end="")






  '''footer'''
  print(f'{"="*75}\n')