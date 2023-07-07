# Casting adalah merubah tipe data satu ke tipe data yang lainnya 
# tipe data ada tipe int, float, string, bool
import os
os.system('cls')
## DATA INTEGER
print("------INT------")
data_int = 101
print("data", data_int, "type = ", type(data_int))

data_float  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int) # akan false jika int bernilai 0, dan akan true jika tidak bernilai 0
print("data", data_float, "type = ", type(data_float))
print("data", data_str, "type = ", type(data_str))
print("data", data_bool, "type = ", type(data_bool))

## DATA FLOAT
print("-----FLOAT-----")
data_float = 101.87
print("data", data_float, "type = ", type(data_float))

data_int    = int(data_float) #dibulatkan ke bawah
data_str    = str(data_float)
data_bool   = bool(data_float) 
print("data", data_int, "type = ", type(data_int))
print("data", data_str, "type = ", type(data_str))
print("data", data_bool, "type = ", type(data_bool))

## DATA BOOLEAN
print("-----BOOL----")
data_bool = True
print("data", data_bool, "type = ", type(data_bool))

data_int    = int(data_bool)
data_str    = str(data_bool)
data_float  = float(data_bool) 
print("data", data_int, "type = ", type(data_int))
print("data", data_str, "type = ", type(data_str))
print("data", data_float, "type = ", type(data_float))

## DATA STRING
print("-----STR----")
data_str = "666"
print("data", data_str, "type = ", type(data_str))

data_int    = int(data_str) # string harus angka
data_bool   = bool(data_str) # false jika 0
data_float  = float(data_str) # string harus angka
print("data", data_int, "type = ", type(data_int))
print("data", data_bool, "type = ", type(data_bool))
print("data", data_float, "type = ", type(data_float))

print("halodek")



