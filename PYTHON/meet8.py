# Perbandingn (lanjutan

# +++++3------9+++++
MasukanUser = float(input("masukan bilangan \nkurang dari 3 atau \nlebih dari 10: "))
print(MasukanUser)

# ----cek kurang dari 3
kurDar =(MasukanUser < 3)
print ("Kurang dari 3 =", kurDar)

# ----cek lebih dari 9
lebDar =(MasukanUser > 9)
print ("lebih dri 9 =", lebDar)

# ----cek sekaligus lebih dan kurang dari
betul = kurDar or lebDar
print("Pengecekan final adalah :", betul)

# ------4+++++++14-------
MasukanUser = float(input("masukan bilangan antara 4 dan 14 :"))
print(MasukanUser)

hasil = (4 <= MasukanUser <=14)
print(hasil)


# -------5+++++++++9------------------12+++++++++++++30------------- PR