def input_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input bukan angka, coba lagi.")


def input_pilihan(valid_opsi, pesan="Pilih: "):
    valid_opsi = {str(o) for o in valid_opsi}
    while True:
        s = input(pesan).strip()
        if s in valid_opsi:
            return int(s)
        print(f"Input tidak valid. Pilihan yang tersedia: {sorted(valid_opsi)}")


# =================
# NOTE :
# c = Celcius
# k = Kelvin
# f = Fahrenheit
# r = Reamur
# =================


def to_c_from_f(f):
    return (f - 32) * 5 / 9


def to_c_from_r(r):
    return r * 5 / 4


def to_c_from_k(k):
    return k - 273.15


def from_c_to_f(c):
    return c * 9 / 5 + 32


def from_c_to_r(c):
    return c * 4 / 5


def from_c_to_k(c):
    return c + 273.15


def konversi_suhu():
    print("==============================================")
    print("WORKSHOP PEMROGRAMAN DASAR")
    print("Selamat Datang di Program Konversi Suhu Sederhana")
    print("==============================================")
    print("1. Celcius")
    print("2. Reamur")
    print("3. Fahrenheit")
    print("4. Kelvin")

    pilih = input_pilihan(
        {1, 2, 3, 4}, "Masukkan satuan yang akan dikonversi (1/2/3/4): "
    )

    # Menaruh label
    label = {1: "Celcius", 2: "Reamur", 3: "Fahrenheit", 4: "Kelvin"}[pilih]
    print(f"\n=={label}==")

    if pilih == 1:  # pilihan ke 1
        c = input_angka("Suhu Celcius = ")
        print("\nMau diubah ke satuan suhu yang mana ?")
        print("1. Reamur")
        print("2. Fahrenheit")
        print("3. Kelvin")
        tujuan = input_pilihan({1, 2, 3}, "Pilih = ")
        if tujuan == 1:
            hasil = from_c_to_r(c)
            tujuan = "reamur"
        elif tujuan == 2:
            hasil = from_c_to_f(c)
            tujuan = "fahrenheit"
        else:
            hasil = from_c_to_k(c)
            tujuan = "kelvin"

    elif pilih == 2:  # pilihan ke 2
        r = input_angka("Suhu Reamur = ")
        c = to_c_from_r(r)
        print("\nMau diubah ke satuan suhu yang mana ?")
        print("1. Celcius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        tujuan = input_pilihan({1, 2, 3}, "Pilih = ")
        if tujuan == 1:
            hasil = c
            tujuan = "celcius"
        elif tujuan == 2:
            hasil = from_c_to_f(c)
            tujuan = "fahrenheit"
        else:
            hasil = from_c_to_k(c)
            tujuan = "kelvin"

    elif pilih == 3:  # pilihan ke 3
        f = input_angka("Suhu Fahrenheit = ")
        c = to_c_from_f(f)
        print("\nMau diubah ke satuan suhu yang mana ?")
        print("1. Celcius")
        print("2. Reamur")
        print("3. Kelvin")
        tujuan = input_pilihan({1, 2, 3}, "Pilih = ")
        if tujuan == 1:
            hasil = c
            tujuan = "celcius"
        elif tujuan == 2:
            hasil = from_c_to_r(c)
            tujuan = "reamur"
        else:
            hasil = from_c_to_k(c)
            tujuan = "kelvin"

    else:  # pilihan ke 4
        k = input_angka("Suhu Kelvin = ")
        c = to_c_from_k(k)
        print("\nMau diubah ke satuan suhu yang mana ?")
        print("1. Celcius")
        print("2. Reamur")
        print("3. Fahrenheit")
        tujuan = input_pilihan({1, 2, 3}, "Pilih = ")
        if tujuan == 1:
            hasil = c
            tujuan = "celcius"
        elif tujuan == 2:
            hasil = from_c_to_r(c)
            tujuan = "reamur"
        else:
            hasil = from_c_to_f(c)
            tujuan = "fahrenheit"

    print(f"\nSuhu {tujuan} =  {hasil:.12f}\n")  # presisi mirip contoh


def MenuUtama():
    print("==============================================")
    print("WORKSHOP PEMROGRAMAN DASAR")
    print("Selamat Datang di Program Konversi Suhu Sederhana")
    print("==============================================")
    print("1. Konversi Suhu")
    print("2. Keluar")


while True:
    MenuUtama()

    m = input_pilihan({1, 2}, "Pilih menu (1/2): ")
    if m == 1:
        konversi_suhu()
    elif m == 2:
        print("Terima kasih, program selesai.")
        break
    input("Tekan Enter untuk kembali ke menu...")
