def caesar_cipher_step_by_step(text, shift):
    encrypted_text = ""
    print(f"=====================================")
    print(f"=== PROSES ENKRIPSI CAESAR CIPHER ===")
    print(f"=====================================")
    print(f"Teks Asli   : {text}")
    print(f"Nilai Shift : {shift}\n")
    
    # Bab 4: Algoritma Loop (Iterasi O(n) pada plaintext)
    for char in text:
        # Bab 1: Logika IF (Kondisi logis untuk filter karakter)
        if char.isalpha():
            # Bab 5: Aritmetika Mod (Menentukan base ASCII)
            base = ord('A') if char.isupper() else ord('a')
            char_index = ord(char) - base
            
            # Proses Pergeseran
            shifted_index = char_index + shift
            
            # Bab 5: Aritmetika Mod (Kongruensi mod 26)
            final_index = shifted_index % 26
            
            # Hasil Huruf Baru
            new_char = chr(final_index + base)
            encrypted_text += new_char
            
            # Output Detail Proses (Analisis)
            print(f"Huruf: {char} → Angka: {char_index}")
            print(f"  Proses: ({char_index} + {shift}) = {shifted_index}")
            print(f"  Modulo: {shifted_index} % 26 = {final_index}")
            print(f"  Huruf Baru: {new_char}\n")
        else:
            # Jika bukan huruf, karakter tetap (Spasi, angka, dsb)
            encrypted_text += char
            print(f"Karakter '{char}' bukan huruf, tidak diubah.\n")
            
    print(f"=====================================")
    print(f"Hasil Akhir Enkripsi (Ciphertext): {encrypted_text}")
    print(f"=====================================\n")
    return encrypted_text

# Bab 3: Fungsi Invers (Membuktikan Sifat Bijektif)
def caesar_decryption(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Invers dari (x + n) adalah (x - n)
            char_index = ord(char) - base
            final_index = (char_index - shift) % 26
            decrypted_text += chr(final_index + base)
        else:
            decrypted_text += char
    return decrypted_text

# --- EKSEKUSI PROGRAM ---

# Input sesuai referensi gambar
plaintext = "HELLO"
key = 3

# 1. Jalankan Proses Enkripsi
ciphertext = caesar_cipher_step_by_step(plaintext, key)

# 2. Jalankan Proses Dekripsi untuk Membuktikan Bab 3
recovered_text = caesar_decryption(ciphertext, key)

print(f"--- ANALISIS MATEMATIKA DISKRIT (BAB 3) ---")
print(f"Ciphertext      : {ciphertext}")
print(f"Fungsi Invers   : Decrypt('{ciphertext}', {key})")
print(f"Hasil Kembali   : {recovered_text} (Terbukti Sama)")
print(f"-------------------------------------------")