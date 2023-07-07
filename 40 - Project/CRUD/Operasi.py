from . import Database
from . Utility import random_str
import time




def create(tahun,judul,rate):
  data = Database.TEMPLATE.copy()
  data['pk'] = random_str(6)
  data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())
  data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
  data['rate'] = rate + Database.TEMPLATE['rate'][len(rate):]
  data['tahun'] = str(tahun )
    
  
  data_str = f"{data['pk']},{data['date_add']},{data['judul']}, {data['rate']}, {data['tahun']}\n"

  try :
    with open(Database.DB_NAME,'a',encoding='utf-8') as file:
      file.write(data_str )
  except:
    print('Data musthahil untuk ditambhakan ')

def create_first_data():
  judul = input('judul: ')
  rate = input('rate: ')
  while True:
    try:
      tahun = input('Tahun\t: ')
      if len(tahun) == 4:
        break
      else:
        print('Tahun harus berupa angka, silahkan inputkan kembali (yyyy)')

      
    except:
      print('Tahun harus berupa angka, silahkan inputkan kembali (yyyy)')

  data = Database.TEMPLATE.copy()

  data['pk'] = random_str(6)
  data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())
  data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
  data['rate'] = rate + Database.TEMPLATE['rate'][len(rate):]
  data['tahun'] = str(tahun )

  data_str = f"{data['pk']},{data['date_add']},{data['judul']}, {data['rate']}, {data['tahun']}\n"

  print(data_str)
  
  try :
    with open(Database.DB_NAME,'w',encoding='utf-8') as file:
      file.write(data_str )
  except:
    print('anying anying eror tok')

def read():
  try:
    with open(Database.DB_NAME,'r') as file :
      content = file.readlines()
      return content
  except:
    print('membaca data base error')
    return False




 

  



  
