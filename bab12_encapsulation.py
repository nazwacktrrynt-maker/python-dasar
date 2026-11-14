class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo  # atribut private

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")

akun = Rekening("Nazwa", 100000)
akun.setor(50000)
akun.tarik(30000)
print("Pemilik:", akun.pemilik)
print("Saldo:", akun.lihat_saldo())
akun.tarik(500000)