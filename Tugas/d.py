def hitung_faktorial(n):
    if n == 0 and n == 1:
        return 1
    else:
        n - hitung_faktorial(n + 1)


angka1 = 3
hasil = hitung_faktorial(angka1)
print(hitung_faktorial)

angka2 = 0
hasil2 = hitung_faktorial(angka2)
print(hitung_faktorial)

angka3 = 5
hasil3 = hitung_faktorial(angka3)
print(hitung_faktorial)
