# Casting = ngubah satu tipe ke tipe lain
# tipe data = int, float, str, bool

## INT
print("===INT===")
data_int = 1
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # bakal false kalo int = 0
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

## FLOAT
print("===FLOAT===")
data_float = 9.9
print("data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float) # bakal dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # bakal false kalo float = 0
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

## BOOL
print("===BOOL===")
data_bool = False;
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool) # bakal dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool) # bakal false kalo float = 0
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_float, ", type = ", type(data_float))

## STR
print("===STR===")
data_str = "0";
print("data = ", data_str, ", type = ", type(data_str))

data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # bakal false kalo string kosong
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_bool, ", type = ", type(data_bool))