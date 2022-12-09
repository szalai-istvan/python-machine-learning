def encryptChar(char, shift):
    if not char.isalpha():
        return char
    ascii = ord(char) - ord('A')
    ascii += shift
    ascii = ascii % 26
    return chr(ascii + ord('A'))

def decryptChar(char, shift):
    return encryptChar(char, -1 * shift)

def encrypt(text, shift):
    result = ''
    for char in text:
        result = result + encryptChar(char, shift)
    return result

def decrypt(text, shift):
    return encrypt(text, -1 * shift)