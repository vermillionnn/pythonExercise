from random import randint, randrange

user = ['Shin Ryujin', 'Hwang Yeji']
idNumber = ['417123456789','123456789741']
age = ['20','21']
address = ['456 Ramyeon Street, Gyeonggi-do, South Korea','765 Toothless Street, Harujong-il, South Korea']
noReg = ['S123456789','H987654321']

print('===========================================================================================')
print('///////////////////////////////////////////////////////////////////////////////////////////')
print('===========================================================================================')
print('         Selamat Datang, Silakan masukkan data Anda untuk melakukan registrasi')
print('===========================================================================================\n')

userName = str(input('Masukkan Nama Anda: '))
user.append(userName)
userID = str(input('Masukkan Nomor ID Anda: '))
idNumber.append(userID)
userAge = int(input('Masukkan Umur Anda: '))
age.append(userAge)
userAddr = str(input('Masukkan Alamat Anda: '))
address.append(userAddr)

def randomizeDigits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

nineDigits = str(randomizeDigits(9))
userNameCap = userName[0][0].capitalize()
userReg = userNameCap + nineDigits
noReg.append(userReg)

print('\n===========================================================================================')
print('Terima kasih telah melakukan registrasi\nNomor Registrasi anda adalah:',userReg)
print('===========================================================================================')
print('///////////////////////////////////////////////////////////////////////////////////////////')
print('===========================================================================================')
print('Cek User Terdaftar')
print('===========================================================================================')

for number, name in enumerate(user,1):
    print(number, name)