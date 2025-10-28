# membua fungsi dengan parameter *nama
def saam(*nama):
    i=0
    print('Halo', end=' ')
    while len(nama) > i:
        print(nama[i], end=' ')
        i += 1
# mengisi masing masing parameter dengan tipe data string
saam('Aldo', 'Budi', 'Cici')
saam('Doni', 'Eka', 'Fani', 'Gina')