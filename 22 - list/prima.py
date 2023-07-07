# angka = int(input('masukkan angka :'))

# if angka == 1:
#   print('bukan bilangan prima')
# for i in range(1, angka + 1):
#   if angka % i == 0:
#     print(i)


import os 
os.system('cls')

data = []
angka = int(input('masukkan angka :'))

for i in range(1, angka + 1):
  if angka % i == 0:
    data.append(i)
print (data)
if len(data) > 2:
  print ("Bukan Prima")
else:
  print ("Prima") 




  
   



