import json
import os
import time

# =========================
# 🔑 Password Strength Check
# =========================
def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        return "Strong"
    else:
        return "Medium"

# =========================
# 🔐 Algorithm 1 (Key Shift)
# =========================
def algo1_encrypt(text, key):
    return ''.join(chr((ord(c) + ord(key[i % len(key)])) % 256) for i, c in enumerate(text))

def algo1_decrypt(text, key):
    return ''.join(chr((ord(c) - ord(key[i % len(key)])) % 256) for i, c in enumerate(text))

# =========================
# 🔐 Algorithm 2 (Reverse + Shift)
# =========================
def algo2_encrypt(text):
    return ''.join(chr((ord(c) + 5) % 256) for c in text[::-1])

def algo2_decrypt(text):
    return ''.join(chr((ord(c) - 5) % 256) for c in text)[::-1]

# =========================
# 🔐 Algorithm 3 (Multi-Layer)
# =========================
def algo3_encrypt(text, key):
    return algo2_encrypt(algo1_encrypt(text, key))

def algo3_decrypt(text, key):
    return algo1_decrypt(algo2_decrypt(text), key)

# =========================
# 💾 Save / Load JSON
# =========================
def save_data(data, filename="data.json"):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("✅ Data saved successfully.")
    except Exception as e:
        print("❌ Save Error:", e)

def load_data(filename="data.json"):
    try:
        if not os.path.exists(filename):
            print("❌ File not found.")
            return None
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        print("❌ Load Error:", e)

# =========================
# 📂 File Encryption
# =========================
def encrypt_file(filename, key, algo):
    try:
        if not os.path.exists(filename):
            print("❌ File not found.")
            return

        with open(filename, "r") as f:
            data = f.read()

        encrypted = apply_encryption(data, key, algo)

        new_file = "encrypted_" + filename
        with open(new_file, "w") as f:
            f.write(encrypted)

        print("✅ File encrypted:", new_file)

    except Exception as e:
        print("❌ File Encryption Error:", e)

def decrypt_file(filename, key, algo):
    try:
        if not os.path.exists(filename):
            print("❌ File not found.")
            return

        with open(filename, "r") as f:
            data = f.read()

        decrypted = apply_decryption(data, key, algo)

        new_file = "decrypted_" + filename
        with open(new_file, "w") as f:
            f.write(decrypted)

        print("✅ File decrypted:", new_file)

    except Exception as e:
        print("❌ File Decryption Error:", e)

# =========================
# 🔄 Apply Encryption / Decryption
# =========================
def apply_encryption(text, key, algo):
    if algo == "1":
        return algo1_encrypt(text, key)
    elif algo == "2":
        return algo2_encrypt(text)
    elif algo == "3":
        return algo3_encrypt(text, key)
    else:
        return None

def apply_decryption(text, key, algo):
    if algo == "1":
        return algo1_decrypt(text, key)
    elif algo == "2":
        return algo2_decrypt(text)
    elif algo == "3":
        return algo3_decrypt(text, key)
    else:
        return None

# =========================
# 🖥 MAIN CLI
# =========================
def main():
    encrypted_data = ""

    while True:
        print("\n===== 🔐 Ultimate Encryption Tool =====")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Save Encrypted Data")
        print("4. Load & Decrypt Data")
        print("5. Encrypt File")
        print("6. Decrypt File")
        print("7. Exit")

        choice = input("Select option: ")

        # 🔐 Encrypt
        if choice == "1":
            text = input("Enter text: ")
            key = input("Enter password key: ")

            strength = check_password_strength(key)
            print("Password Strength:", strength)

            print("\nChoose Algorithm:")
            print("1. Key Shift")
            print("2. Reverse Shift")
            print("3. Multi-Layer")

            algo = input("Choice: ")

            encrypted_data = apply_encryption(text, key, algo)

            if encrypted_data:
                print("🔒 Encrypted:", encrypted_data)
            else:
                print("❌ Invalid Algorithm")

        # 🔓 Decrypt
        elif choice == "2":
            text = input("Enter encrypted text: ")
            key = input("Enter password key: ")

            print("\nChoose Algorithm:")
            print("1. Key Shift")
            print("2. Reverse Shift")
            print("3. Multi-Layer")

            algo = input("Choice: ")

            decrypted = apply_decryption(text, key, algo)

            if decrypted:
                print("🔓 Decrypted:", decrypted)
            else:
                print("❌ Invalid Algorithm")

        # 💾 Save
        elif choice == "3":
            if not encrypted_data:
                print("❌ No data to save.")
                continue

            data = {
                "encrypted_text": encrypted_data,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            save_data(data)

        # 📂 Load
        elif choice == "4":
            data = load_data()
            if data:
                key = input("Enter key: ")

                print("\nChoose Algorithm:")
                print("1. Key Shift")
                print("2. Reverse Shift")
                print("3. Multi-Layer")

                algo = input("Choice: ")

                print("🔓 Decrypted:", apply_decryption(data["encrypted_text"], key, algo))

        # 📄 Encrypt File
        elif choice == "5":
            filename = input("Enter file name: ")
            key = input("Enter key: ")

            print("Choose Algorithm (1/2/3): ")
            algo = input()

            encrypt_file(filename, key, algo)

        # 📄 Decrypt File
        elif choice == "6":
            filename = input("Enter encrypted file name: ")
            key = input("Enter key: ")

            print("Choose Algorithm (1/2/3): ")
            algo = input()

            decrypt_file(filename, key, algo)

        # ❌ Exit
        elif choice == "7":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option")

# =========================
# 🚀 Run
# =========================
if __name__ == "__main__":
    main()