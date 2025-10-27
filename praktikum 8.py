def prima(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def daftar_prima(jumlah):
    hasil = []
    angka = 2
    while len(hasil) < jumlah:
        if prima(angka):
            hasil.append(angka)
        angka += 1
    return hasil

def cetak_segitiga(m):
    semua_prima = daftar_prima(m * (m + 1) * 4)

    while semua_prima and m > 0:
        for i in range(1, m + 1):
            baris = []
            for j in range(i):
                baris.append(str(semua_prima.pop(0) % 10))
            print(" ".join(baris))
        for i in range(m - 1, 1, -1):
            baris = []
            for j in range(i):
                baris.append(str(semua_prima.pop(0) % 10))
            print(" ".join(baris))
        m -= 1
m = int(input("m: "))
cetak_segitiga(m)