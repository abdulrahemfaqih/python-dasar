# operator bitwise


a = 10
b = 20

# bitwise 0R (|)
c = a | b
print('--------OR-------')
print('nilai a :',a,', binary :', format (a,'08b'))
print('nilai b :',b,', binary :', format (b,'08b'))
print('-------------------------------(|)')
print('nilai c :',c,', binary :', format (c,'08b'))

# bitwise AND (&)  
c = a & b
print('\n--------AND-------')
print('nilai a :',a,', binary :', format (a,'08b'))
print('nilai b :',b,', binary :', format (b,'08b'))
print('-------------------------------(&)')
print('nilai c :',c,', binary :', format (c,'08b'))

# bitwise XOR (^)  
c = a ^ b
print('\n--------XOR-------')
print('nilai a :',a,', binary :', format (a,'08b'))
print('nilai b :',b,', binary :', format (b,'08b'))
print('-------------------------------(^)')
print('nilai c :',c,', binary :', format (c,'08b'))

# bitwise not (~) 
c = ~a
print('\n--------NOT-------')
print('nilai c :',c,', binary :', format (c,'08b'))
print('-------------------------------(~)')


# operator keanggotaan
print('\n')
nama = 'abdul rahem faqih '
member = 'a' in nama 
print('a in nama=', member)
list_huruf = ['a','b','d','u','l']
member = 'a' not in list_huruf
print('a in list huruf:', member)


