vokal = ['a','i','u','e','o']
konsonan = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

huruf = str(input('Masukkan huruf = '))
if huruf in vokal:
    print(huruf,'adalah huruf vokal')
elif huruf in konsonan:
    print(huruf,'adalah huruf konsonan')
else:
    print('Input salah!')