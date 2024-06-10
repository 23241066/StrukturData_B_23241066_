# penjumlahan dan pengurangan

MasukanRumus = input ("Penjumlahan = 1 / pengurangan = 2 : " )

if MasukanRumus == "1" :
    print("anda memasuki program penjumlahan")
    MasukanAngka1= int(input("Masukkkan Biilangan 1 :"))
    MasukanAngka2 = int(input("Masukan Bilangan 2 :"))
    nilai = (MasukanAngka1 + MasukanAngka2)
    print("hasil", nilai)
elif MasukanRumus == "2" :
    print("anda memasuki program pengurangan")
    MasukanAngka1= int(input("Masukan bilangan 1 :"))
    MasukanAngka2 = int(input("Masukan bilangan 2 :"))
    nilai = (MasukanAngka1 - MasukanAngka2)
    print("hasil", nilai)
else :
    print ("Salah, anda tidak memilih program")
print("program selesai")