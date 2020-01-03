# This function intends to encrypt plaintext using Caesar Cipher


def CaesarEncrypt():
    plainText = input("Plaintext: ")
    key = input("Key: ")
    cipher = ""
    for letter in plainText:
        if 'a' <= letter <= 'z':
            # ord(letter) - ord('a') gives the index in alphabetical sequence
            # + int(key) gives the encrypted index
            letter = chr((ord(letter) - ord('a') + int(key)) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - ord('A') + int(key)) % 26 + ord('A'))
        cipher += letter
    return cipher

while True:
    print("Ciphertext: " + CaesarEncrypt() + '\n')
