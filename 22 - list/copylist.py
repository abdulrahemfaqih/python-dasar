## TEKNIK MENDUPLIKAT LIST

a = ['saya', 'kamu', 'dia']
print(f'a = {a}')

b = a
print(f'b = {b}')

# merubah member dari a

# akan merubah kedua list

a[2] = 'loe'
a[1] = 'gua'

a.sort()
print(f'a yang sudah di rubah =\n{a}')
print(f'b yang sudah di rubah =\n{b}')

# address list a dan b

print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(a))}')
'''
  list a dan b jika (a=b, b=a) --> (bukan mengcopy) akan menghasilkan address yang sama,oleh karena itu jika kita merubah member a otomatis list b juga akan berubah, begitupun sebaliknya, agar itu semua tidak terjadi gunakan copy list  
'''

# mwnduplikat list dengan copy
print('\n- membuat duplikat c menggunakan a.copy() -')

c = a.copy()


print(f'c ={c}')



print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(a))}')
print(f'address c = {hex(id(c))}') #addresnya beda karena menggunakan copy()

print(f'a  =\n{a}')
print(f'b  =\n{b}') 
print(f'c  =\n{c}')

# kita ubah data 1
c[1] = 'ente'
print(f'a  ={a}')
print(f'b  ={b}') 
print(f'c  ={c}') 


