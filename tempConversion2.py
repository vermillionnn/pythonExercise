print("\nPROGRAM KONVERSI TEMPERATUR\n")

print("[1] Celcius\n[2] Reamur\n[3] Fahrenheit\n[4] Kelvin\nApa yang ingin anda input?")
inputSuhu = int(input("= "))

if inputSuhu == 1:
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

elif inputSuhu == 2:
    reamur = float(input('Masukkan suhu dalam reamur: '))
    print('Suhu adalah', reamur, "R")
    #celcius
    celcius = (5/4) * reamur
    print('Suhu dalam Celcius adalah', celcius, "C")
    # fahrenheit
    fahrenheit = ((9/4) * reamur) + 32
    print('Suhu dalam Fahrenheit adalah', fahrenheit, "F")
    # kelvin
    kelvin = ((5/4) * reamur) + 273
    print('Suhu dalam Kelvin adalah', kelvin, "K")

elif inputSuhu == 3:
    fahrenheit = float(input('Masukkan suhu dalam fahrenheit: '))
    print('Suhu adalah', fahrenheit, "F")
    #celcius
    celcius = (5/9) * (fahrenheit - 32)
    print('Suhu dalam Celcius adalah', celcius, "C")
    # reamur
    reamur = (4/9) * (fahrenheit - 32)
    print('Suhu dalam Reamur adalah', reamur, "R")
    # kelvin
    kelvin = ((5/9) * (fahrenheit - 32)) + 273
    print('Suhu dalam Kelvin adalah', kelvin, "K")

elif inputSuhu == 4:
    kelvin = float(input('Masukkan suhu dalam kelvin: '))
    print('Suhu adalah', kelvin, "K")
    #fahrenheit
    fahrenheit = (9/5) * (kelvin - 273) + 32
    print('Suhu dalam fahrenheit adalah', fahrenheit, "F")
    # reamur
    reamur = (4/5) * (kelvin - 273)
    print('Suhu dalam Reamur adalah', reamur, "R")
    # celcius
    celcius = kelvin - 273
    print('Suhu dalam Celcius adalah', celcius, "C")

else:
    print("Input yang anda masukkan salah!")