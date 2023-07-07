from . import Operasi

DB_NAME = 'data.txt'

TEMPLATE = {
  'pk'      : 'XXXXXX',
  'date_add': 'yyyy-mm-dd',
  'judul'   : 50*' ',
  'rate'    : 50*' ',
  'tahun'   : 'yyyy'
}

def init_console():

  try:
    with open(DB_NAME,'r') as file:
      print('Database tersedia, init done!')

  except:
    print('database tidak ditemukan, silahkan membuat databse baru')
    Operasi.create_first_data()

   
     




