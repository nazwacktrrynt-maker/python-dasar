# List: urutan data yang bisa diubah
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
buah[0] = "anggur"
print("List:", buah)
print("Jumlah:", len(buah))

# Tuple: urutan data yang tidak bisa diubah
koordinat = (10, 20)
print("Tuple:", koordinat)
print("x =", koordinat[0])

# Set: kumpulan data unik tanpa urutan
angka = {1, 2, 2, 3, 3, 3}
angka.add(4)
print("Set:", angka)