# Fungsi tanpa parameter
def sapa():
    print("Halo dari fungsi!")

# Fungsi dengan parameter
def perkenalan(nama, kelas):
    print("Nama saya", nama, "dari kelas", kelas)

# Fungsi dengan return
def tambah(a, b):
    return a + b

# Fungsi dengan nilai default
def salam(nama="teman"):
    print("Selamat datang,", nama)

sapa()
perkenalan("Nazwa", "XI RPL")
hasil = tambah(5, 7)
print("Hasil tambah:", hasil)
salam()
salam("Nazwa")