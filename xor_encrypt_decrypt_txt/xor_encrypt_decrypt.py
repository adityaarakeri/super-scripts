from os import path

def XOR_cipher(string, key):
    encrypted = ""

    for i in range(len(string)):
        encrypted += chr(ord(string[i]) ^ ord(key[i % len(key)]))

    return encrypted

def check_path(path_to_file):
    return path.exists(path_to_file)

def read_path():
    print("Enter file's directory: ")
    path_to_file = input()
    if not check_path(path_to_file):
        print("File doesn't exist.")
        read_path()
    return path_to_file

def read_key():
    print("Enter a KEY: ")
    key = input()
    return key


data = {"path": read_path(), "key": read_key()}

read_file = open(data["path"], 'r')

changed = ""
for line in read_file:
    changed += XOR_cipher(line, data["key"])

read_file.close()

write_file = open(data["path"], "w")

print(changed)

write_file.write(changed)
write_file.close()

print("Done")

