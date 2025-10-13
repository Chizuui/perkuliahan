mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "Gender": "L",
    "menikah": False,
    "hobi": ["membaca", "bermain"],
    "kuliah" : {
        "jurusan": "Jurusan teknologi informasi",
        "prodi": "D3 Teknik Komputer"
    }
}

# print(mahasiswa)

#mengakses item pada dictionary
#menggunakan get()
print('Nama Mahasiswa:', mahasiswa.get("nama"))

# menggunakan kurung siku []
print ('Umur Mahasiswa:', mahasiswa["umur"])

# menggunakan fungsi berantai untuk dictionary bertingkat
print('Jurusan Mahasiswa:', mahasiswa.get("kuliah").get("jurusan"))

# menggunakan kurung siku di kedua dua nya
print('Prodi Mahasiswa:', mahasiswa["kuliah"]["prodi"])