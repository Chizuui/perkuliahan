# Variabel global untuk menyimpan data
# Ini adalah 'state' program, terpisah dari fungsi.
# Berbeda dengan 'self.data_mahasiswa' yang terikat pada objek.
data_mahasiswa = []


def tampilkan_data():
    print("\n--- Daftar Data Tersimpan ---")

    # Langsung mengakses variabel GLOBAL 'data_mahasiswa'
    if not data_mahasiswa:
        print("Belum ada data yang tersimpan.")
    else:
        # Menampilkan data sesuai format
        for i, data in enumerate(data_mahasiswa, start=1):
            print(f"{i}. {data['nama']}, {data['alamat']}")
    print("-----------------------------")


# Ini juga FUNGSI biasa
def tambah_data():
    print("\n--- Menu 1: Tambah Data ---")
    nama = input("Masukkan data nama: ")
    alamat = input("Masukkan data alamat: ")

    # Langsung memodifikasi variabel GLOBAL
    data_mahasiswa.append({"nama": nama, "alamat": alamat})
    print("\nData baru berhasil ditambahkan!")


# FUNGSI biasa
def ubah_data():
    print("\n--- Menu 2: Ubah Data ---")

    # Memanggil FUNGSI global lainnya
    tampilkan_data()

    if not data_mahasiswa:
        print("Data kosong, tidak ada yang bisa diubah.")
        return

    try:
        pilihan_str = input("Pilih data yang akan dirubah : ")
        pilihan = int(pilihan_str)
        index = pilihan - 1

        if 0 <= index < len(data_mahasiswa):
            print(
                f"Anda akan mengubah data ke-{pilihan}: {data_mahasiswa[index]['nama']}"
            )
            nama_baru = input("Masukkan nama baru: ")
            alamat_baru = input("Masukkan alamat baru: ")

            # Langsung memodifikasi variabel GLOBAL
            data_mahasiswa[index] = {"nama": nama_baru, "alamat": alamat_baru}
            print("\nData berhasil diubah!")
        else:
            print("Nomor data invalid.")

    except ValueError:
        print("Input Invalid. Masukkan Angka.")


# FUNGSI biasa
def hapus_data():
    print("\n--- Menu 3: Hapus Data ---")

    tampilkan_data()

    if not data_mahasiswa:
        print("Data kosong, tidak ada yang bisa dihapus.")
        return

    try:
        pilihan_str = input("Pilih data no data yang akan dihapus : ")
        pilihan = int(pilihan_str)
        index = pilihan - 1

        if 0 <= index < len(data_mahasiswa):
            # Langsung memodifikasi variabel GLOBAL
            data_yang_dihapus = data_mahasiswa.pop(index)
            print(f"\nData '{data_yang_dihapus['nama']}' berhasil dihapus.")
        else:
            print("Nomor data invalid.")

    except ValueError:
        print("Input Invalid. Masukkan Angka.")


# FUNGSI utama untuk menjalankan program
def jalankan_program():
    while True:
        print("\nMenu")
        print("1. Tambah data")
        print("2. Ubah data")
        print("3. Hapus data")
        print("4. Tampil data")
        print("5. Keluar")  # Tambahan kecil

        pilihan = input("Pilihlah no menu diatas: ")

        # Memanggil FUNGSI global, bukan method objek
        if pilihan == "1":
            tambah_data()  # Bukan app.tambah_data()
        elif pilihan == "2":
            ubah_data()  # Bukan app.ubah_data()
        elif pilihan == "3":
            hapus_data()  # Bukan app.hapus_data()
        elif pilihan == "4":
            tampilkan_data()  # Bukan app.tampilkan_data()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == "5":
            print("Program selesai.")
            break  # Keluar dari loop
        else:
            print("Pilihan invalid. Pilih nomor 1-5.")


# Langsung panggil FUNGSI global untuk memulai program
jalankan_program()
