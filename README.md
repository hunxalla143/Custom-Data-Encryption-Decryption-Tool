# Custom-Data-Encryption-Decryption-Tool
## Project Overview

This project is a Python-based Command Line Interface (CLI) application designed to securely encrypt and decrypt data using custom-built algorithms. It simulates real-world data protection systems by implementing multi-layer encryption techniques, password-based security, and file handling features.

---

## Objectives

* To design a secure encryption and decryption system
* To implement custom cryptographic logic (not relying on built-in libraries like base64)
* To simulate real-world data protection mechanisms
* To provide hands-on experience with file handling and modular programming

---

## Features

### Core Features

* Encrypt plain text using custom algorithms
* Decrypt encrypted text back to original form
* Reversible encryption logic
* CLI-based interactive interface

### Security Features

* Password/key-based encryption
* Password strength checker (Weak / Medium / Strong)
* Multi-layer encryption support

### Encryption Algorithms

The tool provides multiple encryption techniques:

1. **Key Shift Algorithm**

   * Uses ASCII shifting based on a user-defined key
   * Each character is transformed using the corresponding key character

2. **Reverse Shift Algorithm**

   * Reverses the text
   * Applies a fixed character shift

3. **Multi-Layer Encryption**

   * Combines Key Shift + Reverse Shift
   * Provides stronger obfuscation and security

---

## Encryption Logic (Concept)

* **Encryption:**
  Character ASCII values are modified using key-based shifting and transformation layers

* **Decryption:**
  Reverse operations are applied in correct order to retrieve original data

---

## File Handling

* Save encrypted data in JSON format
* Load stored encrypted data
* Decrypt saved data using correct key and algorithm
* Timestamp included with saved data

---

## File Encryption Support

* Encrypt `.txt` files
* Decrypt previously encrypted files
* Automatically generates:

  * `encrypted_<filename>`
  * `decrypted_<filename>`

---

## User Interface (CLI Menu)

```
1. Encrypt Text
2. Decrypt Text
3. Save Encrypted Data
4. Load & Decrypt Data
5. Encrypt File
6. Decrypt File
7. Exit
```

---

## How to Run

### Requirements

* Python 3.x installed

### Steps

```bash
# Run the program
python main.py
```

Follow on-screen menu instructions.

---

## Sample JSON Output

```json
{
    "encrypted_text": "ÃØÛ...",
    "timestamp": "2026-04-29 14:30:00"
}
```

---

## Error Handling

* Invalid menu selection handling
* File not found protection
* Safe encryption/decryption execution
* Invalid algorithm detection

---

## Project Structure

```
project-folder/
│
├── main.py
├── data.json
└── README.md
```

---

## Bonus Features Implemented

* ✔ Password-based encryption
* ✔ Multi-layer encryption
* ✔ Password strength validation
* ✔ File encryption & decryption
* ✔ Timestamped storage
* ✔ Multiple algorithm selection

---

## Future Enhancements

* GUI version using Tkinter
* Advanced encryption (AES)
* Support for images and PDFs
* User authentication system
* Encryption history tracking

---

## Author

**Hunzalla AJab**

---

## License

This project is for educational and academic purposes.
