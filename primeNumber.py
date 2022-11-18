angka = int(input('Masukkan bilangan = '))

if angka > 1:
    for i in range(2,angka):
        if angka % i == 0:
            print(angka,'bukan bilangan prima')
            print(i,'dikali',angka//i,'adalah',angka)
            break
    else:
        print(angka,'adalah bilangan prima')

else:
    print(angka,'bukan bilangan prima')
