# kurung kurawal
setNomor = {1, 2, 3, 4, 5}
print (setNomor)

#dengan fungsi set()
setString = set (('senin', 'selasa', 'rabu', 'kamis', 'Jumat'))
print (setString)

#set kosong dengan fungsi set dan bukan kurawal
setKosong = set([])
print (setKosong)

#tidak dapat berisi item yang duplikat
SetDuplicate = {1, 2, 3, 3, 4, 4, 5}
print (SetDuplicate)

# dengan tipe data yang berbeda
setMix = {1.5,2.5,3.5,'coba', (4,5,6)}
print (setMix)

# list tidak bisa menjadi aggota set karena list bersifat mutable
setList = {1.5, 2.5, 3.5, 'coba', [4, 5, 6]}
print (setList)