try :
    age = int(input("Masukkan umur Anda: "))

    if (age >= 17):
        kerja = input("Apakah Anda sudah bekerja atau masih kuliah? (kerja/kuliah): ").lower()
        if kerja == "kerja":
            print("Selamat! Anda sudah dewasa dan bekerja.")
        elif kerja == "kuliah":
            print("Anda sudah dewasa dan masih kuliah.")
        else:
            print("Input tidak valid")
    elif (4 < age < 17):
        print("Anda masih Seorang siswa.")
    else:
        print("Anda masih Anak-anak.")

except:
    print("Input tidak valid, masukkan angka saja.")