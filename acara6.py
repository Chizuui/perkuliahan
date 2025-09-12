angka1=20
type(angka1)
angka2=5.5
type(angka2)
angka3=1+2j
type(angka3)
angka4="Hello"
type(angka4)
angka5=True
type(angka5)
angka6=[1,2,3,4,5]
type(angka6)
angka7=(1,2,3,4,5)
type(angka7)
angka8=range(6)
type(angka8)
angka9={"name":"John", "age":30}
type(angka9)
angka10={"apple", "banana", "cherry"}
type(angka10)
angka11=frozenset({"apple", "banana", "cherry"})
type(angka11)
angka12=bytes(5)
type(angka12)
angka13=bytearray(5)
type(angka13)
angka14=memoryview(bytes(5))
type(angka14)
print(angka1, angka2, angka3, angka4, angka5, angka6, angka7, angka8, angka9, angka10, angka11, angka12, angka13, angka14)
del(angka4)
print("angka4 telah dihapus")
print(angka1, angka2, angka3, angka5, angka6, angka7, angka8, angka9, angka10, angka11, angka12, angka13, angka14)
# print(angka4) # This will raise an error because angka4 has been deleted

