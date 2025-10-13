# Fungsi untuk penjumlahan
def add(x, y):
    return x + y

# Fungsi untuk pengurangan
def subtract(x, y):
    return x - y

# Fungsi untuk perkalian
def multiply(x, y):
    return x * y

# Fungsi untuk pembagian
def divide(x, y):
    # Memastikan tidak ada pembagian dengan nol
    if y == 0:
        return "Error! Pembagian dengan nol tidak bisa."
    return x / y

print("Pilih operasi.")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

while True:
    # Mengambil input dari pengguna
    choice = input("Masukkan pilihan (1/2/3/4): ")

    # Mengecek apakah pilihan valid
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Cek apakah pengguna ingin lanjut
        next_calculation = input("Mau coba lagi? (ya/tidak): ")
        if next_calculation.lower() != "ya":
            break
    
    else:
        print("Pilihan tidak valid")