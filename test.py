bergerak = True
while bergerak:
    command = input("Masukkan perintah (maju, mundur, belok kiri, belok kanan, berhenti): ").lower()
    if command == "maju":
        print("Robot bergerak maju.")
    elif command == "mundur":
        print("Robot bergerak mundur.")
    elif command == "belok kiri":
        print("Robot berbelok ke kiri.")
    elif command == "belok kanan":
        print("Robot berbelok ke kanan.")
    elif command == "berhenti":
        print("Robot berhenti.")
        bergerak = False
    else:
        print("Perintah tidak dikenali. Silakan coba lagi.")