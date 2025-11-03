def tambah(x, y):
    return x + y


def kurang(x, y):
    return x - y


def kali(x, y):
    return x * y


def bagi(x, y):
    return x / y


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


def tampil_menu():
    print("==============================================")
    print("WORKSHOP PEMROGRAMAN DASAR")
    print("Selamat Datang di Program Kalkulator Sederhana")
    print("==============================================")
    print("Silahkan Pilih Opsi Operasi kalkulator")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")


while True:
    tampil_menu()

    pilih = input_pilihan()

    num1 = input_angka("Masukkan bilangan pertama: ")
    num2 = input_angka("Masukkan bilangan kedua: ")

    if pilih == "1":
        print(num1, "+", num2, "=", tambah(num1, num2))
    elif pilih == "2":
        print(num1, "-", num2, "=", kurang(num1, num2))
    elif pilih == "3":
        print(num1, "*", num2, "=", kali(num1, num2))
    elif pilih == "4":
        print(num1, "/", num2, "=", bagi(num1, num2))

    input("Tekan Enter untuk kembali ke menu...")
    print()
