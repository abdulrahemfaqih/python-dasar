# tipe data : angka satuan ( integer )



data_integer = 1
print("data : ", data_integer, ", bertipe :", type( data_integer))

# tipe data : angka dengan koma ( float )
data_float = 1.6
print("data : ", data_float, ", bertipe :", type( data_float))

# tipe data : kumpulan karakter ( stirng )
data_string = "odading"
print("data : ", data_string, ", bertipe :", type( data_string))

# tipe data : biner true/false ( boolean)
data_bool = False
print("data : ", data_bool, ", bertipe :", type( data_bool))

## tipe data khusus

#bilangan kompleks
data_complex = complex (5,7,)
print("data : ", data_complex, ", bertipe :", type( data_complex))

# tipe data bahasa c

from ctypes import c_double, c_char, c_long 
data_c_double = c_double(121.4)
print("data : ", data_c_double, ", bertipe :", type( data_c_double))
