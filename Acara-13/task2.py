# 2. Buat sebuah nasted set, dan tampilkan isinya satu per satu

jurusan = ("Teknik", "Teknologi Informasi", "Kesehatan")

prodi = ("Management informasi kesehatan", "Teknik Komputer", "Teknik Energi Terbarukan")

# mengjonversikan tuple menjadi frozenset agar bisa dimasukkan ke dalam  set lain
jurusan_set = frozenset(jurusan)
prodi_set = frozenset(prodi)
# membuat nested set

data_kampus = {
    "Jurusan",
    jurusan_set,
    prodi_set,
    "Prodi" # Elemen string tambahan
}

for elemen in data_kampus:
    # Mengecek apakah elemen adalah frozenset (sub-koleksi)
    if isinstance(elemen, frozenset):
        print(f"\n--- List (Frozenset) ---")
        for item in elemen:
            print(f"  -> {item}") # Menampilkan isi frozenset
        print("-" * 30)
    else:
        # Elemen biasa (string)
        print(f"Tipe Data: {elemen}")

