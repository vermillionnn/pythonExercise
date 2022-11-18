print('[CALCULATOR]')
while True:
    print('[1] (+)  Penjumlahan ')
    print('[2] (-)  Pengurangan')
    print('[3] (x)  Perkalian')
    print('[4] (/)  Pembagian')
    print('[5] (^)  Eksponen/pangkat')
    print('[6] (%)  Modulus/sisa')
    print('[7] (//) Floor division')

    while True:
        userInput = int(input('= '))
        if userInput in range(1,8):
            break
        print('Input salah!')

    # penjumlahan
    def tambah(a,b):
        operasi = '+'
        hasil = a + b
        print('\nHasil:\n',a,operasi,b,'=',hasil)

    # pengurangan
    def kurang(a,b):
        operasi = '-'
        hasil = a - b
        print('\nHasil:\n',a,operasi,b,'=',hasil)

    # perkalian
    def kali(a,b):
        operasi = 'x'
        hasil = a * b
        print('\nHasil:\n',a,operasi,b,'=',hasil)

    # pembagian
    def bagi(a,b):
        operasi = '/'
        hasil = a / b
        print('\nHasil:\n',a,operasi,b,'=',hasil)

    # eksponen/pangkat
    def pangkat(a,b):
        operasi = '^'
        hasil = a ** b
        print('\nHasil:\n',a,operasi,b,'=',hasil)

    # modulus
    def modulus(a,b):
        operasi = '%'
        hasil = a % b
        print('\nHasil:\n',a,operasi,b,'=',hasil)

    # floor division
    def floorDiv(a,b):
        operasi = '//'
        hasil = a // b
        print('\nHasil:\n',a,operasi,b,'=',hasil)

    #main program
    a = float(input('\nAngka 1 = '))
    b = float(input('Angka 2 = '))

    if userInput == 1:
        tambah(a,b)
    elif userInput == 2:
        kurang(a,b)
    elif userInput == 3:
        kali(a,b)
    elif userInput == 4:
        bagi(a,b)
    elif userInput == 5:
        pangkat(a,b)
    elif userInput == 6:
        modulus(a,b)
    elif userInput == 7:
        floorDiv(a,b)

    while True:
        restart = str(input('\nApakah anda ingin menghitung lagi? [y/n]\n= '))
        if restart in ('y','n'):
            break
        else:
            print('Input salah!')
    if restart == 'y':
        continue
    else:
        print('. . . EXIT')
        break
