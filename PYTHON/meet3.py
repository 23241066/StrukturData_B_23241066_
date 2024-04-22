# contoh tipe data (interger) : Angka satuan
bil_interger = 1 
print(type(bil_interger))
print("type data dari bil_integer adalah" ,type(bil_interger))

# contoh bilangan (float) : bilangan desimal
bil_float = 2.5
print(type(bil_float))
print("type data dari bil_float adalah" ,type(bil_float))

# contoh bilangan (string) : kumpulan karakter 
bil_string = '2.5'
print(type(bil_string))
print("type data dari bil_string adalah" ,type(bil_string))

# contoh bilangan (boolean) : biner, o,1, True False
bil_bol = True
print(type(bil_bol))
print("type data dari bil_bool adalah" ,type(bil_bol))

# tipe data dari bahasa 
from ctypes import c_double
bil_double = c_double(5000000)
print("type data dari bil_double adalah" ,type(bil_double))