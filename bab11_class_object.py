class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        print("Halo, nama saya", self.nama, "dari kelas", self.kelas)

siswa1 = Siswa("Nazwa", "XI RPL")
siswa2 = Siswa("Raka", "XI RPL")

siswa1.perkenalan()
siswa2.perkenalan()
print("Nama siswa 1:", siswa1.nama)