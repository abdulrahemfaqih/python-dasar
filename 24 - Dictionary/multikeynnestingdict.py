# MILTI KEY AND NESTING DICTIONARY
import os
os.system('cls')
# MEMBUAT DAFTAR LIST 
import datetime

mahasiswa1 = {
  'nama'  : 'abdul rahem faqih',
  'nim'   : '220411100029',
  'prodi' : 'teknik informatika',
  'lahir' : datetime.datetime(2003,12,26),
  'IPS'   : 3.8,
  'lulus' : True,
}
mahasiswa2 = {
  'nama'  : 'muhammad faris wafda',
  'nim'   : '220411100029',
  'prodi' : 'teknik informatika',
  'lahir' : datetime.datetime(2003,12,25),
  'IPS'   : 1.8,
  'lulus' : False,
}
mahasiswa3 = {
  'nama'  : 'farish ilham syahrani',
  'nim'   : '220411100166',
  'prodi' : 'teknik informatika',
  'lahir' : datetime.datetime(2003,12,24),
  'IPS'   : 2.8,
  'lulus' : True,
}
mahasiswa4 = {
  'nama'  : 'gantara efrin lover',
  'nim'   : '220411100168',
  'prodi' : 'teknik informatika',
  'lahir' : datetime.datetime(2003,12,24),
  'IPS'   : 3.1,
  'lulus' : True,
}
mahasiswa5 = {
  'nama'  : 'angga yu nanda',
  'nim'   : '220411100100',
  'prodi' : 'sistem informasi  ',
  'lahir' : datetime.datetime(2004,9,24),
  'IPS'   : 3.3,
  'lulus' : True,
}

data_mahasiswa = {
  '1' : mahasiswa1,
  '2' : mahasiswa2,
  '3' : mahasiswa3,
  '4' : mahasiswa4,
  '5' : mahasiswa5
}

print(
  f'{"no" : <8} {"nama" : <27} {"NIM" : <12} {"prodi" : <14} {"lahir" : <8} {"IPS" : <4} {"lulus" : <10}'
)
print('-'*85)

for mahasiswa in data_mahasiswa.keys():
  KEY  = mahasiswa
  NAMA  = data_mahasiswa[KEY]['nama' ]
  NIM   = data_mahasiswa[KEY]['nim'  ]
  PRODI = data_mahasiswa[KEY]['prodi']
  LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
  IPS   = data_mahasiswa[KEY]['IPS'  ]
  LULUS = data_mahasiswa[KEY]['lulus']

  print(
  f'{KEY : <3} {NAMA : <27} {NIM : <12} {PRODI : <17} {LAHIR : <9} {IPS : <5} {LULUS : <10}'
)

