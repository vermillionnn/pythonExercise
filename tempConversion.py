print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius: '))
print('Suhu adalah', celcius, "C")

# reamur
reamur = (4/5) * celcius
print('Suhu dalam Reamur adalah', reamur, "R")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('Suhu dalam Fahrenheit adalah', fahrenheit, "F")

# kelvin
kelvin = celcius + 273
print('Suhu dalam Kelvin adalah', kelvin, "K")

# KELVIN TO FAHRENHEIT AND VICE VERSA

print("\n====PROGRAM KONVERSI FAHRENHEIT KE KELVIN DAN VICE VERSA====\n")

fahrenheit = float(input('Masukkan suhu dalam Fahrenheit:'))

kelvin = (fahrenheit + 459.67) * (5/9)
print('Suhu dalam Kelvin adalah:', kelvin, "K")

kelvin = float(input('Masukkan suhu dalam Kelvin:'))

fahrenheit = (9/5) * (kelvin - 273.15) + 32
print('Suhu dalam Fahrenheit adalah', fahrenheit, "F")