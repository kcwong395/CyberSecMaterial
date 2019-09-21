# This function intends to decrypt Caesar ciphertext by brute forcing all possible key


def CaesarBFA(cipherText):
    for key in range(26):
        print(str(key) + ": ", end='')
        for letter in cipherText:
            if 'a' <= letter <= 'z':
                letter = chr((ord(letter) - ord('a') - int(key)) % 26 + ord('a'))
            elif 'A' <= letter <= 'Z':
                letter = chr((ord(letter) - ord('A') - int(key)) % 26 + ord('A'))
            print(letter, end='') # end='' let the output stay at the same line
        print()


while True:
    cipherText = input("Cipher text: ")
    print("\nPossible plain texts:")
    CaesarBFA(cipherText)
    print('\n')
