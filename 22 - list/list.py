# # LIST  

# # Kumpulan data numbers
dataAngka= [1,23,4,5,6,7,]
print(dataAngka)

# Kumpulan data string 
dataBuah = [
'apel' ,'mangga',
'pisang', 'cherry' ,
'pepeya'
]
print(dataBuah)

# kumpulan data boolean 

dataBool = [False, True,
False, True]
print(dataBool)

# data campuran 
dataCampur = [1,2,3,
'sia',True ]
print(dataCampur)

# cara alternatif menggunakan list 
# pake range

dataRange = range(0,100,5)
dataList = list(dataRange)
print(dataList)

# membuat list dengan for loop 

listPakeFor = [
i**10 for i in range(0,11)
]
print(listPakeFor)

# membuat list dengan for dan if

listDenganForIf = [
i for i in range(0,11)
if i !=5
]
print(listDenganForIf)

# ganjil tok
listDenganForIf = [
i for i in range(0,11)
if i%2 !=0
]
print(listDenganForIf)

# genap tok tok
listDenganForIf = [
i for i in range(0,11)
if i%2 == 0
]
print(listDenganForIf)
print()


list_with_for = [
  i for i in range(1,50)
  if i % 2 == 0 and i % 3 == 0
]
print(list_with_for)


print()











