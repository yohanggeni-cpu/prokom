def cetak_garis(tgaris, n):    
    garis = tgaris * n
    print(garis)
    print(varBelumTerdefinisi)
    pass    # Akan mengabaikan jika error, agar bagian lain program tetap bisa jalan

def cetakBiodata(nama, email):
    print("Data Pengguna :")
    cetak_garis("=",20)
    print(nama)
    print(email)
    cetak_garis("-",20)
    
# Bagian Utama Program
nama = "Priyandari"
email = "emailku@smun.ac.id"
cetakBiodata(nama, email)

# Fungsi lambda
x = lambda a : a + 10   # a pertama adalah pendefinisian parameter, a kedua adalah penggunaan variabel a pada proses
print(x(8)) # Nilai 5 adalah argument yang dikirim