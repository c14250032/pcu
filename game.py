matriks = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]
    ]
def map():
    import random
    global matriks
    posisi = []
    for i in range(5):
        for j in range(5):
            posisi.append((i,j))
    random.shuffle(posisi)

    matriks[posisi[0][0]][posisi[0][1]] = "P"
    matriks[posisi[1][0]][posisi[1][1]] = "E"
    for i in range(2, 6):
        matriks[posisi[i][0]][posisi[i][1]] = "X"

def tampilkan_map():
    for baris in matriks:
        print(" ".join(baris))
    print()
def movement_atas():
    for i in range(5):
        for j in range(5):
            if matriks[i][j] == "P":
                if i == 0:
                    print("Anda keluar dari map")
                    return "kalah"
                if i > 0 and matriks[i - 1][j] == ".":
                    matriks[i][j] = "."
                    matriks[i-1][j] = "P"
                elif i > 0 and matriks[i - 1][j] == "E":
                    matriks[i][j] = "."
                    matriks[i - 1][j] = "P"
                    tampilkan_map()
                    print("Selamat kamu menang!!!")
                    return "menang"
                return
def movement_kanan():
    for i in range(5):
        for j in range(5):
            if matriks[i][j] == "P":
                if j == 4:
                    print("Anda keluar dari map")
                    return "kalah"
                if j < 4 and matriks[i][j + 1] == ".":
                    matriks[i][j] = "."
                    matriks[i][j + 1] = "P"
                elif j < 4 and matriks[i][j + 1] == "E":
                    matriks[i][j] = "."
                    matriks[i][j + 1] = "P"
                    print("Selamat kamu menang!!!")
                    return "menang"
                return
def movement_bawah():
    for i in range(5):
        for j in range(5):
            if matriks[i][j] == "P":
                if i == 4:
                    print("Anda keluar dari map")
                    return "kalah"
                if i < 4 and matriks[i + 1][j] == ".":
                    matriks[i][j] = "."
                    matriks[i + 1][j] = "P"
                elif i < 4 and matriks[i + 1][j] == "E":
                    matriks[i][j] = "."
                    matriks[i + 1][j] = "P"
                    print("Selamat kamu menang!!!")
                    return "menang"
                return
def movement_kiri():
    for i in range(5):
        for j in range(5):
            if matriks[i][j] == "P":
                if j == 0:
                    print("Anda keluar dari map")
                    return "kalah"
                if j > 0 and matriks[i][j - 1] == ".":
                    matriks[i][j] = "."
                    matriks[i][j - 1] = "P"
                elif j > 0 and matriks[i][j - 1] == "E":
                    matriks[i][j] = "."
                    matriks[i][j - 1] = "P"
                    print("Selamat kamu menang!!!")
                    return "menang"
                return
print("Tekan Q untuk keluar")
map()
while True:
    tampilkan_map()
    pilihan = input("Masukkan pilihan(W/A/S/D): ").capitalize()
    hasil = None
    if pilihan == "W":
        hasil = movement_atas()
    elif pilihan == "A":
        hasil = movement_kiri()
    elif pilihan == "S":
        hasil = movement_bawah()
    elif pilihan == "D":
        hasil = movement_kanan()
    elif pilihan == "Q":
        break
    if hasil == "menang":
        break
    elif hasil == "kalah":
        print("Kamu kalah")
        break

