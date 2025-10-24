# Variabel global untuk menyimpan data 
# Kita menggunakan list (daftar) dari dictionary
# Contoh: [{"nama": "Yogiswara", "alamat": "taman gading 3"}]
data_mahasiswa = []

def tampilkan_data():
    """
    Fungsi untuk menampilkan semua data yang tersimpan.
    Sesuai dengan langkah di Tampilan 2 (menu 2, 3) dan Tampilan 2 (menu 4).
    [cite: 18, 29, 34]
    """
    print("\n--- Daftar Data Tersimpan ---")
    if not data_mahasiswa:
        print("Belum ada data yang tersimpan.")
    else:
        # Menampilkan data sesuai format, misal: "1. Yogiswara, taman gading 3" [cite: 19]
        for i, data in enumerate(data_mahasiswa, start=1):
            print(f"{i}. {data['nama']}, {data['alamat']}")
    print("-----------------------------")

def tambah_data():
    """
    Fungsi untuk menu 1: Tambah data [cite: 4, 9]
    """
    print("\n--- Menu 1: Tambah Data ---")
    nama = input("Masukkan data nama: ")       # [cite: 10]
    alamat = input("Masukkan data alamat: ")   # [cite: 12]
    
    # Simpan data ke dalam list [cite: 14, 15]
    data_mahasiswa.append({"nama": nama, "alamat": alamat})
    
    print("\nData baru berhasil ditambahkan!")
    # Program akan otomatis kembali ke menu utama setelah fungsi selesai [cite: 16]

def ubah_data():
    """
    Fungsi untuk menu 2: Ubah data [cite: 5, 17]
    """
    print("\n--- Menu 2: Ubah Data ---")
    # Langkah 1: Menampilkan data [cite: 18]
    tampilkan_data()
    
    if not data_mahasiswa:
        print("Data kosong, tidak ada yang bisa diubah.")
        return # Kembali ke menu utama

    try:
        # Meminta input nomor data yang akan diubah [cite: 22, 23]
        pilihan_str = input("Pilih data yang akan dirubah : ")
        pilihan = int(pilihan_str)
        
        # Konversi ke index list (dimulai dari 0)
        index = pilihan - 1
        
        # Validasi apakah nomor yang dipilih ada di dalam list
        if 0 <= index < len(data_mahasiswa):
            # Langkah 2: Meminta input data baru [cite: 24]
            print(f"Anda akan mengubah data ke-{pilihan}: {data_mahasiswa[index]['nama']}")
            nama_baru = input("Masukkan nama baru: ")       # [cite: 25]
            alamat_baru = input("Masukkan alamat baru: ")   # [cite: 26]
            
            # Langkah 3: Lakukan proses perubahan data [cite: 27]
            data_mahasiswa[index] = {"nama": nama_baru, "alamat": alamat_baru}
            print("\nData berhasil diubah!")
            # Program akan otomatis kembali ke menu utama [cite: 27]
        else:
            print("Nomor data tidak valid.")
            
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def hapus_data():
    """
    Fungsi untuk menu 3: Hapus data [cite: 6, 28]
    """
    print("\n--- Menu 3: Hapus Data ---")
    # Langkah 1: Menampilkan data [cite: 29]
    tampilkan_data()
    
    if not data_mahasiswa:
        print("Data kosong, tidak ada yang bisa dihapus.")
        return # Kembali ke menu utama
        
    try:
        # Meminta input nomor data yang akan dihapus [cite: 30]
        pilihan_str = input("Pilih data no data yang akan dihapus : ")
        pilihan = int(pilihan_str)
        
        # Konversi ke index list (dimulai dari 0)
        index = pilihan - 1
        
        # Validasi apakah nomor yang dipilih ada di dalam list
        if 0 <= index < len(data_mahasiswa):
            # Langkah 2: Melakukan penghapusan data [cite: 32]
            data_yang_dihapus = data_mahasiswa.pop(index)
            print(f"\nData '{data_yang_dihapus['nama']}' berhasil dihapus.")
            # Program akan otomatis kembali ke menu utama [cite: 32]
        else:
            print("Nomor data tidak valid.")
            
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# --- Program Utama ---
def jalankan_program():
    """
    Fungsi utama untuk menjalankan loop menu.
    """
    while True:
        # Menampilkan Tampilan 1 (Menu Utama) [cite: 2, 3]
        print("\nMenu")
        print("1. Tambah data")  # [cite: 4]
        print("2. Ubah data")    # [cite: 5]
        print("3. Hapus data")   # [cite: 6]
        print("4. Tampil data")  # [cite: 7]
        
        pilihan = input("Pilihlah no menu diatas: ") # [cite: 8]
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            # Tampilan 2 (jika dipilih no 4) [cite: 33]
            # Langkah 1: Tampilkan data [cite: 34]
            tampilkan_data()
            # Langkah 2: Kembali ke menu (setelah user menekan Enter) [cite: 34]
            input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor 1-4.")

# Memulai eksekusi program
if __name__ == "__main__":
    jalankan_program()