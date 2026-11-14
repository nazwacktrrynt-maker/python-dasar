class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan")

class Kucing(Hewan):
    def suara(self):
        print(self.nama, "berbunyi: meong")

class Anjing(Hewan):
    def suara(self):
        print(self.nama, "berbunyi: guk guk")

kucing = Kucing("Mimi")
anjing = Anjing("Doggo")

kucing.makan()
kucing.suara()
anjing.makan()
anjing.suara()