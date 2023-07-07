import os
os.system('cls')


# duar = int(input('duar: '))
 
# faktor = []

# for lala in range(1,duar + 1):
#   if duar % lala == 0:
#     faktor.append(lala)
#   else: 
#     pass

# if len(faktor) > 2:
#   print('komposit')
# else: 
#   print('not komposit')



b = int(input('duar: '))

x = 1
factor = 0

while x <= b :
  if b % x == 0:
    factor += 1
  x += 1

if factor <= 2:
  print('this num not composit')
else:
  print('this num is composit')





  

 
