# operasi logika boolean 
# not, or, and, xor
import os
os.system('cls')


# Not
x = True
z = not x
print('data x =', x)
print('ketika varibel x telah di not')
print('data z =', z)
print()
print()
# or (jika salah satunya true maka menghasilkan true)
x = False
y = False
z = x or y # ketika dua-duanya False
print(x, 'or', y, '=', z)
x = True 
y = False 
z = x or y # ketika salah satunya True
print(x, 'or', y, '=', z)
x = True
y = True
z = x or y # ketika dua duanya True
print(x, 'or', y, '=', z)
print()
print()

# and (jika dua buah nilai true, maka hasilnya true)
x = False
y = False
z = x and y # ketika dua duanya False
print(x,  'and', y, '=', z)
x = True 
y = False 
z = x and y # ketika salah satunya True
print(x,  'and', y, '=', z)
x = True
y = True
z = x and y # ketika dua duanya True
print(x,  'and', y, '=', z)



print()
print()

# xor (akan true, jika salah satu nilainya true)
print('\n===xor===\n')
x = False
y = False
z = x ^ y
print(x,  'xor', y, '=', z)
print('\n')
x = True 
y = False 
z = x ^ y
print(x,  'xor', y, '=', z)
print('\n')
x = False
y = True
z = x ^ y
print(x,  'xor', y, '=', z)
print('\n')
x = True
y = True
z = x ^ y
print(x,  'xor', y, '=', z)
print ('\n')
