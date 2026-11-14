try:
    angka = int("abc")
except ValueError:
    print("Error: input bukan angka")

try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Error: tidak bisa dibagi nol")
finally:
    print("Selesai")
