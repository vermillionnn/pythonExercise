def Palindrome(kata):
    reverse = ''.join(reversed(kata))

    if kata == reverse:
        return True
    return False

kata = str(input('Masukkan kata: '))
ans = Palindrome(kata)

if (ans):
    print('Palindrome')
else:
    print('Bukan Palindrome')