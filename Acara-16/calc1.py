def tambah(x, y):
    return x + y


def kurang(x, y):
    return x - y


def kali(x, y):
    return x * y


def bagi(x, y):
    return x / y


print("Pilih operasi Kalkulasi")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilih = input("Masukkan pilihan (1/2/3/4): ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

if pilih == "1":
    print(num1, "+", num2, "=", tambah(num1, num2))

elif pilih == "2":
    print(num1, "-", num2, "=", kurang(num1, num2))

elif pilih == "3":
    print(num1, "*", num2, "=", kali(num1, num2))

elif pilih == "4":
    print(num1, "/", num2, "=", bagi(num1, num2))

else:
    print("Pilihan tidak valid")


# pilihan = input("Masukkan pilihan (1/2/3/4): ")

# if pilihan == "1":
#     num1 = float(input("Masukkan bilangan pertama: "))
#     num2 = float(input("Masukkan bilangan kedua: "))
#     print("Hasil penjumlahan:", tambah(num1, num2))
# elif pilihan == "2":
#     num1 = float(input("Masukkan bilangan pertama: "))
#     num2 = float(input("Masukkan bilangan kedua: "))
#     print("Hasil pengurangan:", kurang(num1, num2))
# elif pilihan == "3":
#     num1 = float(input("Masukkan bilangan pertama: "))
#     num2 = float(input("Masukkan bilangan kedua: "))
#     print("Hasil perkalian:", kali(num1, num2))
# elif pilihan == "4":
#     num1 = float(input("Masukkan bilangan pertama: "))
#     num2 = float(input("Masukkan bilangan kedua: "))
#     print("Hasil pembagian:", bagi(num1, num2))
# else:
#     print("Pilihan tidak valid")
