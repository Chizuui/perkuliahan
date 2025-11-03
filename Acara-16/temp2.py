def konversiSuhu(suhu):
    drjt = int(suhu[:-1])
    inputan = suhu[-1]

    if inputan.upper() == "C":
        hasil1 = float((9 * drjt) / 5 + 32)
        hasil2 = float(drjt + 273.15)
        hasil3 = float(4 / 5 * drjt)
        jenisX = "Celcius"
        jenis1 = "Fahrenheit"
        jenis2 = "Kelvin"
        jenis3 = "Reamur"
        print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
        print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
        print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

    elif inputan.upper() == "F":
        hasil1 = float((drjt - 32) * 5 / 9)
        hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
        hasil3 = float(4 / 9 * (drjt - 32))
        jenisX = "Fahrenheit"
        jenis1 = "Celcius"
        jenis2 = "Kelvin"
        jenis3 = "Reamur"
        print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
        print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
        print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

    elif inputan.upper() == "K":
        hasil1 = float(drjt - 273.15)
        hasil2 = float((drjt - 273.15) * 9 / 5 + 32)
        hasil3 = float(4 / 5 * (drjt - 273))
        jenisX = "Kelvin"
        jenis1 = "Celcius"
        jenis2 = "Fahrenheit"
        jenis3 = "Reamur"
        print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
        print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
        print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

    elif inputan.upper() == "R":
        hasil1 = float((5 / 4) * drjt)
        hasil2 = float((9 / 4 * drjt) + 32)
        hasil3 = float((5 / 4 * drjt) + 273)
        jenisX = "Reamur"
        jenis1 = "Celcius"
        jenis2 = "Fahrenheit"
        jenis3 = "Kelvin"
        print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
        print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
        print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

    else:
        print("Maaf, inputan tidak sesuai. Sesuaikan inputan dengan kriteria yang ada")


# --- Bagian Program Utama ---

i = 0
print("=========================================")
print("WORKSHOP PEMROGRAMAN DASAR")
print("Selamat Datang di Program Konversi Suhu Sederhana")
print("=========================================")

while i == 0:
    temp = input(
        "\nSilahkan masukkan suhu, diikuti satuan suhu (Misal: 0C, 200F, 273K, 60R = "
    )
    konversiSuhu(temp)

    lagi = input("Hitung lagi? (1=ya & 0=tidak) = ")
    if lagi == "1":
        i = 0
    elif lagi == "0":
        i = 1
