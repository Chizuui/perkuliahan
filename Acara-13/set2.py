#buat set baru
numSet = {1, 2, 3}
print (numSet)

#menambah item ke set
numSet.add(4)
print (numSet)

# menguodate item pada set tidak akan update jika item sudah ada
numSet.update([5, 1, 6, 2, 7])
print (numSet)

# menghapus item pada set
numSet.discard(6) #akan error jika item tidak ada
print (numSet)
numSet.remove(7) #akan error jika item tidak ada
print (numSet)

# menghapus item set sebelah kiri dengan pop()
numSet.pop() #akan error jika set kosong
print (numSet)
print (numSet.pop())
print (numSet)

#mengosongkan set
numSet.clear()
print (numSet)