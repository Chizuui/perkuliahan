# variable global
nama = "Desca Rizki Febriant"
golongan = "B"

def sebut():
    # variable local
    nama = "Bara"
    golongan = "A"
    # mengakses variable lokal
    print ('Nama: %s' % nama)
    print ('Golongan: %s' % golongan)

# mengakses variable global
print ('Nama: %s' % nama)
print ('Golongan: %s' % golongan)

# memanggil fungsi sebut
sebut()