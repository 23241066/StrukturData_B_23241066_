#UAS Percabangan Dan perulangan 
nama = input ("Masukan nama : ")

n = 3  # jumlah input yang ingin diulang
for i in range(n):
    print(nama * (i + 1))

if nama == "adam": #Kondisi 1
    print ("Mahasiswa Keren") #Aksi True 1
elif nama == "adam " : #Kondisi 2
    print("Mahasiswa Keren") #Aksi True 2
elif nama == "bima" : #Kondisi 3
    print("Mahasiswa Ganteng") #Aksi True 3
elif nama == "bima " : #Kondisi 4
    print("Mahasiswa Ganteng") #Aksi True 4
elif nama =="ridho" : #Kondisi 5
    print("Mahasiswa Pintar") #Aksi True 5
elif nama =="ridho " : #Kondisi 6
    print("Mahasiswa Pintar") #Aksi True 6
elif nama =="chelly" : #Kondisi 7
    print("Mahasiswa Rajin") #Aksi True 7
elif nama =="chelly " : #Kondisi 8
    print("Mahasiswa Rajin") #Aksi True 8
else :
    print("Bukan Mahasiswa") #Aksi False 1
    print("program selesai")
    
