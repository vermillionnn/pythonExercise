data_integer = 1
print("data : ", data_integer)
print("- bertipe: ", type(data_integer))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe: ", type(data_complex))

# tipe data bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe: ", type(data_c_double))