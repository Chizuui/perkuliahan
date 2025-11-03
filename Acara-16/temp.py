def TampilkanSuhu():
    print("==================================================")
    print("WORKSHOP PEMROGRAMAN DASAR")
    print("Selamat Datang di Program Konversi Suhu Sederhana")
    print("==================================================")
    print("1. Celcius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. Reamur")
    print("Silahkan Pilih Satuan Mana yang akan di Konversi")

def subTampilanSuhu():
    print('Suhu')
def input_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input bukan angka, coba lagi.")


def input_pilihan():
    while True:
        pilih = input("Masukkan pilihan (1/2/3/4: ").strip()
        if pilih.isdigit() and pilih in {"0", "1", "2", "3", "4"}:
            return int(pilih)
        print("Input bukan angka atau tidak valid, coba lagi.")


# def konversiSuhu(suhu):
#     drjt = int(suhu[:-1])
#     inputan = suhu[-1]

#     if inputan.upper() == "C":
#         hasil1 = float((9 * drjt) / 5 + 32)
#         hasil2 = float(drjt + 273.15)
#         hasil3 = float(4 / 5 * drjt)
#         jenisX = "Celcius"
#         jenis1 = "Fahrenheit"
#         jenis2 = "Kelvin"
#         jenis3 = "Reamur"
#         print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
#         print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
#         print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

#     elif inputan.upper() == "F":
#         hasil1 = float((drjt - 32) * 5 / 9)
#         hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
#         hasil3 = float(4 / 9 * (drjt - 32))
#         jenisX = "Fahrenheit"
#         jenis1 = "Celcius"
#         jenis2 = "Kelvin"
#         jenis3 = "Reamur"
#         print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
#         print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
#         print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

#     elif inputan.upper() == "K":
#         hasil1 = float(drjt - 273.15)
#         hasil2 = float((drjt - 273.15) * 9 / 5 + 32)
#         hasil3 = float(4 / 5 * (drjt - 273))
#         jenisX = "Kelvin"
#         jenis1 = "Celcius"
#         jenis2 = "Fahrenheit"
#         jenis3 = "Reamur"
#         print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
#         print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
#         print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

#     elif inputan.upper() == "R":
#         hasil1 = float((5 / 4) * drjt)
#         hasil2 = float((9 / 4 * drjt) + 32)
#         hasil3 = float((5 / 4 * drjt) + 273)
#         jenisX = "Reamur"
#         jenis1 = "Celcius"
#         jenis2 = "Fahrenheit"
#         jenis3 = "Kelvin"
#         print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
#         print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
#         print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")

#     else:
#         print("Maaf, inputan tidak sesuai. Sesuaikan inputan dengan kriteria yang ada")


def suhuCelcius(drjt):
    hasil1 = float(drjt - 273.15)
    hasil2 = float((drjt - 273.15) * 9 / 5 + 32)
    hasil3 = float(4 / 5 * (drjt - 273))
    jenisX = "Celcius"
    jenis1 = "Kelvin"
    jenis2 = "Fahrenheit"
    jenis3 = "Reamur"
    print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
    print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
    print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")


def suhuFahrenheit(drjt):
    hasil1 = float((drjt - 32) * 5 / 9 + 273.15)
    hasil2 = float((drjt - 32) * 5 / 9)
    hasil3 = float((drjt - 32) * 4 / 9)
    jenisX = "Fahrenheit"
    jenis1 = "Kelvin"
    jenis2 = "Celcius"
    jenis3 = "Reamur"
    print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
    print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
    print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")


def suhuKelvin(drjt):
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


def suhuReamur(drjt):
    hasil1 = float(drjt * 5 / 4 + 273.15)
    hasil2 = float(drjt * 9 / 4 + 32)
    hasil3 = float(drjt * 9 / 10)
    jenisX = "Reamur"
    jenis1 = "Kelvin"
    jenis2 = "Fahrenheit"
    jenis3 = "Celcius"
    print(f"{drjt} {jenisX}, ={hasil1:.1f} {jenis1}")
    print(f"{drjt} {jenisX}, ={hasil2:.1f} {jenis2}")
    print(f"{drjt} {jenisX}, ={hasil3:.1f} {jenis3}")


while True:
    TampilkanSuhu()

    pilih = input_pilihan()
