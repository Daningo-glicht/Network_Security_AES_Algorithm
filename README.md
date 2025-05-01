# Implementation of A manual approach to AES encryption in CBC mode 
# AES-128 Encryption in CBC Mode – Manual python Implementation

This repository contains a complete Python implementation of AES-128 in CBC mode, built "from scratch" without using external libraries like 'pycryptodome' for the encryption core. The implementation includes key scheduling, sub-bytes, shift rows, mix columns, padding, and CBC chaining.

##
Name: SATIRTHA SEN 
Roll Number: CS22B1066 
Semester**: 6th Semester  
Institute: National Institute of Technology Puducherry

## Features

- AES-128 with 16-byte key derived from SHA-256 of input
- CBC mode chaining with randomly generated IV
- PKCS#7 padding scheme
- Complete key expansion logic implemented manually
- Byte-wise XOR for block chaining
- Hexadecimal output for ciphertext, IV, and key
- Console-based interactive UI

## How It Works

### Encryption Steps

1. Input plaintext from user
2. Generate a 128-bit key from SHA-256 digest of the input
3. Generate a random 16-byte IV
4. Pad plaintext using PKCS#7
5. Split into 16-byte blocks and encrypt each with:
   - AddRoundKey
   - SubBytes
   - ShiftRows
   - MixColumns (except last round)
6. XOR each plaintext block with previous ciphertext block (CBC)
7. Concatenate and print final ciphertext

### Decryption Steps

1. Use the same key and IV
2. Decrypt each 16-byte block with:
   - InvShiftRows
   - InvSubBytes
   - InvMixColumns
3. XOR with previous ciphertext block
4. Remove PKCS#7 padding
5. Output original plaintext

## Implementation Details

This program follows the Advanced Encryption Standard (AES) as defined for 128-bit keys. It includes:

- Key Expansion: Generates 11 round keys from the initial key using RCON and the S-Box.
- Block Transformation: Each 16-byte block undergoes 10 rounds of AES transformations.
- CBC Mode Logic: Each plaintext block is XORed with the previous ciphertext block before encryption.
- Padding: PKCS#7 ensures the input is a multiple of 16 bytes.
- Decryption: Reverses the encryption process using inverse operations.

All steps are implemented manually in Python rather than using built-in cryptographic packages.

## Usage Example

Run the script using Python 3:

...bash

python aes_cbc_manual.py

## ▶ Output

===================================================
      AES-128 CBC Mode Encryption/Decryption
===================================================
Enter the message to encrypt:
> AES, or Advanced Encryption Standard, is a symmetric encryption algorithm widely used to protect sensitive data. It's a block cipher that encrypts data in blocks of 128 bits using keys of 128, 192, or 256 bits. AES was adopted by the U.S. National Institute of Standards and Technology (NIST) in 2001 to replace the Data Encryption Standard (DES), which was becoming vulnerable to attacks. 

Generating AES Key from SHA-256 (first 16 bytes)...

AES Key (hex): e309617ace87a91f79eaa0d8c4ec2634

IV (hex): be82062540bce812911bf3cadf752108
 
Ciphertext (IV + Cipher, hex):

be82062540bce812911bf3cadf75210862a0e007c1baf5dcf67395228fa86e2fa0eba54c2487adb7b5abdea7899a7748adec37e1ab7c3e7cd5c597069473e0a3be57dcf38309e8687bb2c6ce3d14dfa9ef68e3d27a9a60b861bf097a9eff4038c8dc31cb69ec217a510cb41cb45961be63091be55e94e45e0453c3a49540706d55a6bf95acae2c4bf2c719c345d06ec66ba77b5ee8f8880564df851ea24ee10a734a3ac7dbb94a69913f91250ad4110bb5f685be36f5d3649ad550eccb62c6238bddddd1498a6391db14684b185fc5853a199651261bd3b93eab1c785b48f2bd2f0e496a9be79f40ce6e0b4a64b5805dfd130021388f26f555c6a3c56cf6674a92b726814db95d99b08fa97e77b8fe7dcc16fddc80b82c0e58febd9335c6789b59ca54d02428ba57e1280d40e91ed2937eeca4440d5d2b15434cfaaae5f2c7bfbd4bb5ad3dfaadd38e156b122c3337553cd772f476e8e3e6c3ce83c888c09bd5e146eb268d7e8f49580081fdc4da8b5b4a78ccb0b59b0a638886961549065cf080e56c9926208e13e29e0350c16f29954a4638411c3d6df0b203bd58cac7ca14
 
Starting Decryption...

Decrypted Message:

AES, or Advanced Encryption Standard, is a symmetric encryption algorithm widely used to protect sensitive data. It's a block cipher that encrypts data in blocks of 128 bits using keys of 128, 192, or 256 bits. AES was adopted by the U.S. National Institute of Standards and Technology (NIST) in 2001 to replace the Data Encryption Standard (DES), which was becoming vulnerable to attacks. 
Decryption completed successfully!


## Security Considerations

- Random IV ensures different ciphertexts for the same plaintext
- Key is deterministically derived from SHA-256 hash of input (for demo; not secure in production)
- No authentication (e.g., MAC or HMAC) included – this allows potential ciphertext tampering

## Limitations

- Only supports **AES-128** (no 192 or 256-bit variants)
- No key derivation function (KDF) or password-based encryption
- No GCM/CTR modes for authenticated encryption
- Must securely store the IV along with ciphertext for correct decryption

## Performance Analysis

- Suitable for small messages and demonstration use cases
- Manual operations (e.g., key expansion, mix columns) are slower than hardware-accelerated libraries
- Ideal for educational and assignment-based contexts

## Implementation Output

The demonstration output confirms that:

- AES key expansion, encryption, and decryption are working as expected
- CBC chaining logic is properly applied
- Input messages are recovered exactly after decryption

> This validates the correctness and functionality of the entire pipeline

## References

- [David Wong's Block Breakers: AES Explained](https://davidwong.fr/blockbreakers/aes.html)
- [GeeksForGeeks: Advanced Encryption Standard (AES)](https://www.geeksforgeeks.org/advanced-encryption-standard-aes/)

## Files in This Repository

| File Name           | Description                                
|---------------------|--------------------------------------------
| `aes_cbc_manual.py` | Full Python implementation of AES-128 CBC  
| `README.md`         | This documentation                         
| `CS22B1066_AES_Report.docx` | Assignment report for submission          |

## Educational Note

This implementation is for **learning purposes only**. For any real-world application, always use vetted cryptographic libraries such as:

- [PyCryptodome](https://www.pycryptodome.org/)
- [Cryptography.io](https://cryptography.io/)
