# inputan dari user
# aritmatika 

# belajar inputan
abdul = input("masukan kata : ")
print("isi dari abdul : ", abdul,"bertipe data :", type(abdul)),


# belajar arimatika dasar

# contoh dri penjumlahan +
x = 3
y = 4

hasil = x + y
print (" x + y =", hasil)

# contoh dri pengurangan -
x = 3
y = 4

hasil = x - y
print (" x - y =", hasil)

# contoh dri perkalian *
x = 3
y = 4

hasil = x * y
print (" x * y =", hasil)

# contoh dri pembagian /
x = 3
y = 4

hasil = x / y
print (" x / y =", hasil)

# perpangkatan exponen **
x = 3
y = 4

hasil = x ** y
print (" x ^ y =", hasil)

# modulus %
x = 3
y = 4

hasil = y % x
print (" x % y =", hasil)

# floor division (pembulatan kebawah) //
x = 11
y = 4

hasil = x // y
print (" x // y =", hasil)

# aritmatika prioritas

# () , exponen , perkalian atau pembagian , penjumlahan atau pengurangan

# contoh
a = 3
b = 4 
c = 5

hasil = ( a ** b * (c + a) / b - c % a // b)
print(hasil)