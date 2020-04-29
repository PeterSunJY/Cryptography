# Cryptography
## Summary
This program is used to encode and decode seven kinds of ciphers.
This program runs in the terminal. 
The python3 interpreter is needed.

## Included Files
1. main.py
2. input_text.txt
3. output_text.txt

The main.py file contains all the python codes. The input_text.txt is a file that could allow users to put the input plaintext or ciphertext. The output text will be written into the output_text.txt file. Notice, if the output_file.txt is not empty, the output will overwrite the file which could cause potential risks of data loss.

## Supported Ciphers
1. Generalized Caesar Codes
2. Linear Codes
3. Vigenere Cipher
4. Hill Cipher
5. Autokey Cipher
6. Vernam Cipher
7. RSA Cryptosystem

## Notices
- For the first five ciphers, only the letters will be encrypted. The element other than letters, such as numbers, symbols will be accepted but won't be encrypted. These elements will be directly put into the ciphertext.
- For the Vernam Cipher, only lower case letters will be accepted and encrypted.
- For the RSA, all letters numbers and symbols which in the 128 elements of the ASCII table will be accepted and encrypted. For the decryption part, users must use file input rather than manual input. If the input of encryption or decryption contains elements that are not included in the ASCII table, it has potential risks to cause an error.
