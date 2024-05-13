# tabel kebenaran
# not and or xor

# NOT (Bernilai Kebalikannya)

print("*Logika NOT*")
x = False
y = not x
print('value x =', x)

x = True
y = not x
print('value x =', x)

# OR (Semua Bernilai True Asalkan ada Truenya)
print ("*Logika OR*")

x = False
y = False
z =  x or y
print(x, 'OR', y, '=',z)

x = False
y = True
z =  x or y
print(x, 'OR', y, '=',z)

x = True
y = True
z =  x or y
print(x, 'OR', y, '=',z)

# AND (Semua Bernilai True Ketika Keduanya True)
print ("*Logika AND*")

x = False
y = False
z =  y and x
print(x, 'AND', y, '=',z)

x = False
y = True
z =  x and y
print(x, 'AND', y, '=',z)

x = True
y = True
z =  y and x
print(x, 'AND', y, '=',z)

# XOR (Jika Keduanya Sama maka hasilnya False)
print ("*Logika XOR*")

x = False
y = False
z =  y ^ x
print(x, 'XOR', y, '=',z)

x = False
y = True
z =  x ^ y
print(x, 'XOR', y, '=',z)

x = True
y = True
z =  y ^ x
print(x, 'XOR', y, '=',z)