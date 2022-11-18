def pokok(jumlahJamKerja, gaji):
    gajiPokok = gaji * jumlahJamKerja
    print('Gaji Pokok       : Rp',gajiPokok,'/hari')

def lembur(jumlahJamKerja):
    if jumlahJamKerja > 7:
        jamLembur = jumlahJamKerja - 7
        print('Lembur           :',jamLembur,'jam')
    else:
        jamLembur = 0
        print('Lembur           :',jamLembur,'jam')
    if (jumlahJamKerja >= 9):
        uangTransport = 4000
        print('Transport Lembur : Rp',uangTransport,'/hari')
    else:
        uangTransport = 0
        print('Transport Lembur : Rp',uangTransport,'/hari')

def makan(jumlahJamKerja):
    if jumlahJamKerja >= 8:
        uangMakan = 3500
        print('Uang Makan       : Rp',uangMakan,'/hari')
    else:
        uangMakan = 0
        print('Uang Makan       : Rp',uangMakan,'/hari')

#main program
gaji = 2000
nip = str(input('Masukkan NIP                       : '))
nama = str(input('Masukkan Nama                      : '))
jumlahJamKerja = int(input('Masukkan Jumlah Jam Kerja (perhari): '))

print('\n===============SLIP GAJI===============')
print('NIP              :',nip)
print('Nama             :',nama)
pokok(jumlahJamKerja,gaji)
lembur(jumlahJamKerja)
makan(jumlahJamKerja)
print('=======================================')