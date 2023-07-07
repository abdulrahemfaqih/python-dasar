print('buatlah program menampilkan kotak ')



n = int(input('n = '))

for i in range(1,2*n+1):
  print('*', end = ' ')
print()

for x in range(1, 2 * n - 1):   
  print('*', end = ' ')

  for j in range(1, 2 * n -1):
    print(' ', end = ' ')
  print('*')

for k in range(1, 2 * n + 1): 
  print('*' , end = ' ')
print()






