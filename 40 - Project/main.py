import os
import CRUD as CRUD


if __name__ == '__main__':
  operation_system = os.name

  match operation_system:
    case 'posix': os.system('clear')
    case 'nt': os.system('cls')
  
  print('SELAMAT DATANG DI PROGRAM\n   DATABASE LIST ANIME')
  print('--------------------------')

  # cek database ada atau tidak 
  CRUD.init_console()


  while True:
    match operation_system:
      case 'posix': os.system('clear')
      case 'nt': os.system('cls')
      # pencocokan sistem operasi yang digunakan 


    print('SELAMAT DATANG DI PROGRAM\n   DATABASE LIST ANIME')
    print('--------------------------')
    
    print('1. Read Data')
    print('2. Create Data')
    print('3. Update Data')
    print('4. Delete Data')
    print('5. Exit Program\n')
    print('inpukan angka')

    user_option = input('masukkan opsi: ')

   

    match user_option:
      case '1': CRUD.read_console()
      case '2': CRUD.create_console()
      case '3': CRUD.update_console()
      case '4': print('Delete Data')

   

    tanya = input('apakah selesai? (y/n): ')

    if tanya == 'y' or tanya == 'Y':
      break

  print('program selesai')



