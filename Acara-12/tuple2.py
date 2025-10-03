tupleKosong = ()
tupleSingleton = ('satu',)
tupleSingleton2 = (1,)
tupleSingleton3 = 'satu',
tupleBulan = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni')

#dibuat tanpa kurung
tupleAngka = 1,2,3,4,5,6,7,8,9,10

# menggabungkan 2 tuple menjadi 1
tupleGab = tupleSingleton3 + tupleAngka
print (tupleGab)

#mengakses data tuple
print (tupleBulan[0])
print (tupleBulan[3])
print (tupleBulan[5])
print (tupleAngka[-1])
print (tupleAngka[-3])
print (tupleAngka[-5])