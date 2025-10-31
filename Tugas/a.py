def tampilkanAngka(batas, i=50):
    print(f"Perulangan ke {i}")

    if i == batas:  # jika i sama dengan batas
        print("Selesai.")
        return

    elif i < batas:
        # Jika i lebih kecil
        tampilkanAngka(batas, i + 2)

    elif i > batas:
        # Jika i lebih besar
        tampilkanAngka(batas, i - 2)


print("--- Recrusive Start ---")
tampilkanAngka(60)
print("--- Recrusive End ---")
