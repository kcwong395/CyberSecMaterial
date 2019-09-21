# This function intends to decrypt plaintext with a known key


def CaesarDecrypt():
    cipherText = input("Ciphertext: ")
    key = input("Key: ")
    plainText = ""
    for letter in cipherText:
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) - ord('a') - int(key)) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - ord('A') - int(key)) % 26 + ord('A'))
        plainText += letter
    return plainText

while True:
    print("Plaintext: " + CaesarDecrypt() + '\n')
