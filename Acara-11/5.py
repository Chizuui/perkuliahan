# list minuman dengan 2 dimensi
minuman = [
    ["kopi","susu","teh"],
    ["jus apel","jus melon","jur jeruk"],
    ["es kopi","es campur","es teler"]
]
print(minuman)
print('\n')

# cara mengakses list multidiemnsi
# angka pertama menunjukkan kolom,yang kedua adalah baris
print("menampilkan salah satu menu dengan menunjuk nomer index :")
print(minuman[2][0])
print(minuman[0][1])
print('\n')

# mencetak isi list di dalam list satu persatu
print('\n')
print("menampilkan isi list di dalam list :")
for menu in minuman:
    for menu2 in menu:
        print(menu2)