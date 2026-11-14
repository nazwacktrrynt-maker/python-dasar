from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, jari):
        self.jari = jari

    def luas(self):
        return round(3.14 * self.jari ** 2, 2)

print("Luas persegi:", Persegi(5).luas())
print("Luas lingkaran:", Lingkaran(7).luas())
