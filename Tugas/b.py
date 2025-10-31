def jumlah_deret(n):
    if n == 0:
        return 0
    else:
        return n + jumlah_deret(n - 2)


bilangan = 8
hasil = jumlah_deret(bilangan)
print(f"Jumlah deret dari 1 sampai {bilangan} adalah {hasil}")
