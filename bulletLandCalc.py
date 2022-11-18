import math

phi = 3.14
gravity = 9.8

print('Menghitung Jarak Peluru\n')
sudut = float(input('Masukkan Sudut Penembakan (derajat) = '))
kecepatan = float(input('Masukkan Kecepatan Tembak (m/s) = '))

rad = (sudut * phi) / 180
jarak = (2 * (kecepatan ** 2) * math.sin(rad)) * math.cos(rad) / gravity

print('Jarak Peluru =',jarak,'m')