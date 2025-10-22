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

for key in sorted(mahasiswa):
    print('%s: %s' % (key, mahasiswa[key]))
    
# print('Jumlah key pada variable siswa :', len(mahasiswa))

# print('Apakah dictionary mahasiswa memiliki key nama?')
# print('nama' in mahasiswa)

# print('\nApakah variable siswa TIDAK memiliki key status?')
# print('status' not in mahasiswa)


# # menghaus item
# del mahasiswa ['nama']
# print('Nama Mahasiswa:', mahasiswa.get("nama"))

# # menghapus menggunakan pop
# mahasiswa.pop ('umur')
# print('Umur Mahasiswa:', mahasiswa.get("umur"))

# # menampilkan nilai kembalian data yang saudah dihapus
# gender = mahasiswa.pop('Gender')
# print('jenis kelamin mahasiswa:', gender)

# # mencetak key alamat sekaligus cek
# print('Alamat:', mahasiswa.get("alamat"))

# # menambahkan key alamat ke dalam dict mahasiswa 
# mahasiswa["alamat"] = "jember"

# # mencetak hasil 
# print('Mahasiswa {} beralamat di {}'.format(
#     mahasiswa.get('nama'),
#     mahasiswa.get('alamat')
# ))

# # mengubah nilai item
# print('Nama Awal:', mahasiswa.get("nama"))
# mahasiswa["nama"] = "Budi Santoso"
# print('Nama Setelah Diubah:', mahasiswa.get("nama"))

# #mengakses item pada dictionary
# #menggunakan get()
# print('Nama Mahasiswa:', mahasiswa.get("nama"))

# # menggunakan kurung siku []
# print ('Umur Mahasiswa:', mahasiswa["umur"])

# # menggunakan fungsi berantai untuk dictionary bertingkat
# print('Jurusan Mahasiswa:', mahasiswa.get("kuliah").get("jurusan"))

# # menggunakan kurung siku di kedua dua nya
# print('Prodi Mahasiswa:', mahasiswa["kuliah"]["prodi"])