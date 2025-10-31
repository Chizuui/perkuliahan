# Data Mahasiswa
data_mahasiswa = [
    {"nim": "101", "nama": "Budi", "ipk": 3.2},
    {"nim": "102", "nama": "Ani", "ipk": 3.8},
    {"nim": "103", "nama": "Candra", "ipk": 2.9},
    {"nim": "104", "nama": "Dewi", "ipk": 3.5},
]


# === CONTOH 1: MENCETAK NAMA ===
def cetak_nama_rekursif(list_mhs):
    # 1. Kasus Dasar (Base Case)
    if not list_mhs:
        return

    # 2. Langkah Rekursif (Recursive Step)
    mahasiswa_pertama = list_mhs[0]
    print(f"- {mahasiswa_pertama['nama']} (NIM: {mahasiswa_pertama['nim']})")
    cetak_nama_rekursif(list_mhs[1:])


print("### Daftar Nama Mahasiswa ###")
cetak_nama_rekursif(data_mahasiswa)


# === CONTOH 2: MENGHITUNG IPK > 3.0 ===
def hitung_ipk_di_atas(list_mhs, batas_ipk=3.0):
    # 1. Kasus Dasar (Base Case)
    if not list_mhs:
        return 0

    # 2. Langkah Rekursif (Recursive Step)
    mahasiswa_pertama = list_mhs[0]
    sisa_list = list_mhs[1:]

    jumlah_dari_sisa = hitung_ipk_di_atas(sisa_list, batas_ipk)

    if mahasiswa_pertama["ipk"] > batas_ipk:
        return 1 + jumlah_dari_sisa
    else:
        return 0 + jumlah_dari_sisa


# Menjalankan fungsi
jumlah_lulus = hitung_ipk_di_atas(data_mahasiswa, 3.0)
print(f"\n### Jumlah Mahasiswa dengan IPK > 3.0 ###")
print(f"Total: {jumlah_lulus} mahasiswa")
