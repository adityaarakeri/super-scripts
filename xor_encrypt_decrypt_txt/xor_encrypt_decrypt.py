def XOR_cipher(string, key):
    encrypted = ''

    for i in range(len(string)):
        encrypted += chr(ord(string[i]) ^ ord(key[i % len(key)]))

    return encrypted


def XOR_uncipher(string, key):
    decrypted = ''

    for i in range(len(string)):
        decrypted += chr(ord(string[i]) ^ ord(key[i % len(key)]))
    
    return decrypted

def read_input():
    fine = False
    while not fine:
        print("Choose a mode e(ncrypt)/d(ecrypt): ")
        mode = input()

        print("Enter file's directory: ")
        path = input()

        print("Enter a KEY: ")
        key = input()

