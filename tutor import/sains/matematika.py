'''fungsi tambah'''
def tambah(*data):
  ouput = 0
  for i in data:
    ouput += i 
  return ouput

'''fungsi kali'''
def kali(*data):
  output = 0
  for angka in data:
    ouput *= angka  
  return ouput

'''fungsi bagi'''
def bagi(angka1:int,angka2:int) -> int:
  return angka1/angka2

'''fungsi pengurangan'''
pengurangan = lambda x,y:x-y

'''fungsi pangkat'''
pangkat = lambda angka,pangkat : angka**pangkat


# def tambah():
#   print(1 + 2)


# def tambah(x,y):
#   tambah = x + y
#   return tambah

# x = tambah(1,3)
# print(x)






