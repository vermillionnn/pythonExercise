npm = []
nama = []
uts = []
uas = []
absen = []
tugas = []
akhir = []

jumlahData = int(input('Jumlah Data: '))

for i in range(0,jumlahData):
    print('\nInput Data ke -',i+1)
    npmSiswa = str(input('NPM: '))
    namaSiswa = str(input('Nama: '))
    nilaiUts = float(input('Nilai UTS: '))
    nilaiUas = float(input('Nilai UAS: '))
    nilaiAbsen = float(input('Nilai Absen: '))
    nilaiTugas = float(input('Nilai Tugas: '))
    npm.append(npmSiswa)
    nama.append(namaSiswa)
    uts.append(nilaiUts)
    uas.append(nilaiUas)
    absen.append(nilaiAbsen)
    tugas.append(nilaiTugas)
    nilaiAkhir = (0.3*nilaiUts) + (0.4*nilaiUts) + (0.3*nilaiUas) + (0.1*nilaiAbsen) + (0.2*nilaiTugas)

print('\nNPM','\t','Nama','\t','UTS','\t','UAS','\t','ABSEN','\t','TUGAS','\t','AKHIR')

for i in range(0, jumlahData):
    print(i)
    print(jumlahData)
    print(npm[i],'\t',nama[i],'\t',uts[i],'\t',uas[i],'\t',absen[i],'\t',tugas[i],'\t',akhir[i])