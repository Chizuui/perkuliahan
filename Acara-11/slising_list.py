list_kata = ["mangga", "jambu", "apel", "anggur"]

#mengubah indeks ke 1 pada list_kata
print ("Sebelum diubah:")
list_kata[1] = "rambutan"
print (list_kata)

# menambah list pada liat_kata tapi tidak disimpan
print ('List juga bisa ditambahkan :')
print (list_kata + ["delima", "melon", "pear"])

# menambah list pada list_kata dan disimpan
print ('List juga bisa ditambahkan dan disimpan :')
list_kata += ["delima", "melon", "pear"]
print (list_kata)

# mengali list pada list_kata
print ('List juga bisa dikali :')
print (list_kata * 2)

# memeriksa item pada list
print ('mangga' in list_kata)
print ('salah' not in list_kata)
if "melon" in list_kata:
    print ("Ada melon")