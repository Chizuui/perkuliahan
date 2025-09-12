angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operator == '-':
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == '*':
    hasil = angka1 * angka2S
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error! Tidak bisa membagi dengan nol.")
else:
    print("Operator tidak valid.")
    