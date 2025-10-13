day = ['hari', 'senin', 'selasa', 'maret', 'rabu', 'kamis', 'juni']
print (day)

# menghapus nilai yang sama
print ('menghapus maret dari list :')
day.remove('maret')
print (day)

# menghapus nilai pada indeks tertentu (del)
print ('menghapus indeks ke 0 yaitu hari :')
del day[0]
print (day)

# menghapus nilai pada indeks tertentu (pop)
print ('menghapus indeks ke 4 yaitu juni mneggunakan pop :')
day.pop(4)
print (day)

# menghapus nilai item terakhir pada list yaitu kamis (pop)
print ('menghapus item terakhir pada list yaitu kamis menggunakan pop :')
day.pop()
print (day)

# menghapus nilai yang dihapus menggunakan pop
print ('menghapus nilai yang dihapus menggunakan pop :')
print (day.pop(0))
