class Burung:
    def suara(self):
        print("Burung berkicau")

class Sapi:
    def suara(self):
        print("Sapi melenguh")

class Bebek:
    def suara(self):
        print("Bebek berkwek")

for hewan in [Burung(), Sapi(), Bebek()]:
    hewan.suara()
