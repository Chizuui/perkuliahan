# Variabel global untuk menyimpan data 
# Kita menggunakan list (daftar) dari dictionary

data_mahasiswa = []

def tampilkan_data():
    # Fungsi untuk menampilkan semua data yang tersimpan.
    # Sesuai dengan langkah di Tampilan 2 (menu 2, 3) dan Tampilan 2 (menu 4).

    print("\n--- Daftar Data Tersimpan ---")
    if not data_mahasiswa:
        print("Belum ada data yang tersimpan.")
    else:
        # Menampilkan data sesuai format
        for i, data in enumerate(data_mahasiswa, start=1):
            print(f"{i}. {data['nama']}, {data['alamat']}")
    print("-----------------------------")

def tambah_data():
    # Fungsi untuk menu 1: Tambah data

    print("\n--- Menu 1: Tambah Data ---")
    nama = input("Masukkan data nama: ")
    alamat = input("Masukkan data alamat: ")
    
    # Simpan data ke dalam list [cite: 14, 15]
    data_mahasiswa.append({"nama": nama, "alamat": alamat})
    
    print("\nData baru berhasil ditambahkan!")
    # Program akan otomatis kembali ke menu utama setelah fungsi selesai

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
        # Meminta input nomor data yang akan diubah
        pilihan_str = input("Pilih data yang akan dirubah : ")
        pilihan = int(pilihan_str)
        
        # Konversi ke index list (dimulai dari 0)
        index = pilihan - 1
        
        # Validasi apakah nomor yang dipilih ada di dalam list
        if 0 <= index < len(data_mahasiswa):
            # Langkah 2: Meminta input data baru
            print(f"Anda akan mengubah data ke-{pilihan}: {data_mahasiswa[index]['nama']}")
            nama_baru = input("Masukkan nama baru: ")
            alamat_baru = input("Masukkan alamat baru: ")
            
            # Langkah 3: Lakukan proses perubahan data
            data_mahasiswa[index] = {"nama": nama_baru, "alamat": alamat_baru}
            print("\nData berhasil diubah!")
            # Program akan otomatis kembali ke menu utama
        else:
            print("Nomor data tidak valid.")
            
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def hapus_data():

    print("\n--- Menu 3: Hapus Data ---")

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

def jalankan_program():

    # Fungsi utama untuk menjalankan loop menu.

    while True:
        print("\nMenu")
        print("1. Tambah data")
        print("2. Ubah data")
        print("3. Hapus data")
        print("4. Tampil data")
        
        pilihan = input("Pilihlah no menu diatas: ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
            input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor 1-4.")

    
jalankan_program()