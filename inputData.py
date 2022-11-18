# data yang dimasukkan pasti string

data = input("Masukkan data: ")
print("data =", data, ",type =", type(data))

# kalo mau ngambil int, maka
angka = float(input("Masukkan angka: "))
angka = int(input("Masukkan angka: "))
print("data =", angka, ",type =", type(angka))

# boolean
biner = bool(int(input("Masukkan nilai boolean: ")))
print("data =", biner, ",type =", type(biner))