def cetak_garis(tgaris, n):    
    garis = tgaris * n
    print(garis)
    pass

# Mengatur nilai default parameter
def cetakBiodata(nama, kota = "Yogya"): # nilai default kota adalah Yogya
    print(f"Data Pengguna : {nama}")
    cetak_garis("=",20)
    print(f"Nama : {nama}")
    print(f"Kota : {kota}")
    cetak_garis("-",20)

cetakBiodata("Tobby")
cetakBiodata("Yurike","Solo")