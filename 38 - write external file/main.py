# 1. mode write

with open('data_1.txt','w', encoding='utf-8') as file:
  file.write('barang siapa\nbarang gue\nhahaha')
with open('data_1.txt','w', encoding='utf-8') as file:
  file.write('barang siapa\nbukan barang gue\nhahaha')

# mode write akan menimpa 

# 2. mode append

with open('data_2.txt','a', encoding='utf-8') as file:
  file.write('barang siapa\nbarang gue\nhahaha\n')

with open('data_2.txt','a', encoding='utf-8') as file:
  file.write('barang siapa\nbarang gue\nhahaha')
