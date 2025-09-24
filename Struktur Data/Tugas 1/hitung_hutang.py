def hutang():
    try:
        hutang_awal = float(input("Masukkan jumlah hutang awal: "))
        persen_bunga = float(input("Masukkan persentase bunga per hari (contoh: 2 untuk 2%): "))
        hari = int(input("Masukkan jumlah hari: "))

        # Persentase bunga diubah menjadi desimal lalu dibagi 100
        hutang_akhir = hutang_awal * (1 + (persen_bunga / 100)) ** hari

        # Menampilkan hasil
        print(f"\nData yang di input:")
        print(f"Hutang awal: Rp {hutang_awal:,.2f}")
        print(f"Bunga harian: {persen_bunga}%")
        print(f"Jumlah hari: {hari} hari")
        print("-" * 30)
        print(f"Hutang akhir: Rp {hutang_akhir:,.2f}")

    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka untuk semua nilai.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    hutang()