siswa = {
    "nama": "Nazwa",
    "kelas": "XI RPL",
    "umur": 16
}

print("Data siswa:", siswa)
print("Nama:", siswa["nama"])

# Menambah dan mengubah isi
siswa["sekolah"] = "SMKN 2"
siswa["umur"] = 17

# Menghapus isi
del siswa["kelas"]

# Menampilkan semua key dan value
for kunci, nilai in siswa.items():
    print(kunci, "=", nilai)