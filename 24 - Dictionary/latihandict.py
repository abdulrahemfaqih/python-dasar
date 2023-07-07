import datetime
import os

mahasiswa_template = {
  'nama ' : 'nama',
  'nim  ' : '000000000000',
  'prodi' : 'prodi',
  'ips  ' : 0.00,
  'lahir' : datetime.datetime(1111,11,11),
}

data_mahasiswa = {}

while True :
  os.system('cls')
  print(f'{"SELAMAT DATANG" :^100}')
  print(f'{"DATA MAHASISWA" :^100}')
  print('-'*122)

  mahasiswa = dict.fromkeys(mahasiswa_template.keys())
  print(mahasiswa)

  mahasiswa['nama'] = input('NAMA : ')
  mahasiswa['nim'] = input('NIM : ')
  mahasiswa['prodi'] = input('PRODI : ')
  mahasiswa['ips'] =float(input('IPS : '))
  TAHUN_LAHIR = int(input('TAHUN LAHIR (XXX) : '))
  BULAN_LAHIR = int(input('BULAN (1-12) : ')) 
  TANGGAL_LAHIR = int(input('TANGGAL (1-31) : '))
  mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR),

  data_mahasiswa.update({'key' : mahasiswa})



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
    IPS   = data_mahasiswa[KEY]['ips'  ]

    print(f'{KEY : <3} {NAMA : <27} {NIM : <12} {PRODI : <17} {LAHIR : <9} {IPS : <5} ')
  
  print('\n')
  sudah = input('suda belum? (y/n) ')
  if sudah == 'n':
    break
print('AKHIR DARI PROGRAM')


