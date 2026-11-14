with open("catatan.txt", "w") as f:
    f.write("Halo, ini file pertama\n")
    f.write("Belajar Python itu seru\n")

with open("catatan.txt", "a") as f:
    f.write("Baris tambahan\n")

with open("catatan.txt", "r") as f:
    for baris in f:
        print(baris.strip())
