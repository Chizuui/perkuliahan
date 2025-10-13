angka = [1, 5, 7, 9, 11]

# Mendapatkan jumlah item pada list menggunakan len
print("Jumlah item pada list:")
print(len(angka))

# Mengakses item di akhir list menggunakan append
print("Item terakhir pada list:")
angka.append(13)
print(angka)

# menyisipkan item pada indeks tertentu menggunakan isert
print ('menyisipkan angka 3 pada indeks ke 1 mengguanakan insert:')
indeks =1
angka.insert(indeks, 3)
print(angka)

# menambah list pada list menggunakan extend
print ('menambah list berisi 15, 17, 19 pada list nomor:')
angka.extend([15, 17, 19])
print(angka)

#cek indeks
print("cek angka 1 indeks berapa? angka 2 di indeks keberapa?")
print (angka.index(1))
print (angka.index(2))
