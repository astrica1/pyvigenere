import os

def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def LengthEqualizer(text, key):
    if len(key) == len(text):
        return key
    if len(key) > len(text):
        key = key[ : len(text)]
    else:
        key_length = len(key)
        length_pointer = 0
        while len(key) < len(text):
            key += key[length_pointer % key_length]
            length_pointer += 1
    return key

def CharShifter(text_char, key_char, forward=True):
    char = ''
    char_order = 0
    if forward:
        char_order = ord(text_char) + (ord(key_char) - ord('A'))
    else:
        char_order = ord(text_char) - (ord(key_char) - ord('A'))
    if (char_order <= ord('Z')) and (char_order >= ord('A')):
        char = chr(char_order)
    elif char_order > ord('Z'):
        char = chr(ord('A') + (char_order % (ord('Z') + 1)))
    elif char_order < ord('A'):
        char = chr(ord('Z') - (ord('A') - char_order) + 1)
    return char

def Encryption():
    planeText = input('Plane text: ').upper().replace(' ', '')
    key = input('Key: ').upper().replace(' ', '')
    key = LengthEqualizer(planeText, key)
    cipher = ''
    for i in range(len(planeText)):
        cipher += CharShifter(planeText[i], key[i], True)
    print(cipher)

def Decryption():
    cipher = input('Cipher text: ').upper().replace(' ', '')
    key = input('Key: ').upper().replace(' ', '')
    key = LengthEqualizer(cipher, key)
    planeText = ''
    for i in range(len(cipher)):
        planeText += CharShifter(cipher[i], key[i], False)
    print(planeText)
    
    
def main():
    while True:
        print('Enter \'e\' for Encryption')
        print('Enter \'d\' for Decryption')
        char = input('Application mode: ').lower()
        ClearConsole()
        if char == 'd':
            print('Decryption')
            print('==========\n')
            Decryption()
            exit(0)
        elif char == 'e':
            print('Encryption')
            print('==========\n')
            Encryption()
            exit(0)

if __name__ == "__main__":
    main()