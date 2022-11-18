a = 10
b = 3

# tambah
c = a + b
print(a,'+',b,'=',c)

# kurang
c = a - b
print(a,'-',b,'=',c)

# kali
c = a * b
print(a,'*',b,'=',c)

# bagi
c = a / b
print(a,'/',b,'=',c)

# eksponen (pangkat)
c = a ** b
print(a,'**',b,'=',c)

# modulus (sisa)
c = a % b
print(a,'%',b,'=',c)

# floor division
c = a// b
print(a,'//',b,'=',c)

# prioritas operasi / operational precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

# URUTAN
# 1. () (kurung diitung duluan)
# 2. eksponen
# 3. perkalian/pembagian/modulus/floordivision
# 4. pertambahan/pengurangan
