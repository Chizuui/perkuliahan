data_mahasiswa = []


def show_data():
    print("\n--- Daftar Data Tersimpan ---")
    if not data_mahasiswa:
        print("Belum ada data yang tersimpan.")
    else:
        for index, mahasiswa in enumerate(data_mahasiswa, start=1):
            print(f"{index}. Nama: {mahasiswa['nama']}, Alamat: {mahasiswa['alamat']}")
        print()


def add_data():
    print("\n--- Menambahkan Data Mahasiswa ---")
    nama = input("Nama: ")
    alamat = input("alamat: ")
    data_mahasiswa.append({"nama": nama, "alamat": alamat})
    print("Data berhasil ditambahkan.")


def change_data():
    print("\n--- Mengubah Data Mahasiswa ---")
    if not data_mahasiswa:
        print("Belum ada data yang tersimpan.")
    else:
        show_data()
        index = int(input("Masukkan nomor data yang ingin diubah: ")) - 1
        if 0 <= index < len(data_mahasiswa):
            nama = input("Nama baru: ")
            alamat = input("alamat baru: ")
            data_mahasiswa[index]["nama"] = nama
            data_mahasiswa[index]["alamat"] = alamat
            print("Data berhasil diubah.")
        else:
            print("Nomor data tidak valid.")


def delete_data():
    print("\n--- Menghapus Data Mahasiswa ---")
    if not data_mahasiswa:
        print("Belum ada data yang tersimpan.")
    else:
        show_data()
        index = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
        if 0 <= index < len(data_mahasiswa):
            del data_mahasiswa[index]
            print("Data berhasil dihapus.")
        else:
            print("Nomor data tidak valid.")


def save_data():
    with open("data_mahasiswa.txt", "w") as file:
        for data in data_mahasiswa:
            file.write(f"{data['nama']},{data['alamat']}\n")


def load_data():
    try:
        with open("data_mahasiswa.txt", "r") as file:
            for line in file:
                nama, alamat = line.strip().split(",")
                data_mahasiswa.append({"nama": nama, "alamat": alamat})
    except FileNotFoundError:
        pass


def run_program():
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("5. Simpan Data")
        print("6. Load Data")
        print("7. Keluar")
        choice = input("Pilih menu (1/2/3/4/5/6/7): ")
        if choice == "1":
            add_data()
        elif choice == "2":
            change_data()
        elif choice == "3":
            delete_data()
        elif choice == "4":
            show_data()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "7":
            print("Finished")
            break
        else:
            print("Pilihan tidak valid.")


run_program()
