from hashlib import sha256

file_in = input('File to encrypting / decrypting (file.txt) : ')
file_out = input('Output file name : ')
key = sha256(input('Password : ').encode('utf-8')).digest()

with open(file_in, 'rb') as f_in:
    with open(file_out, 'wb') as f_out:
        i = 0
        while f_in.peek():
            b = bytes([ord(f_in.read(1)) ^ key[i % len(key)]])
            f_out.write(b)
            i += 1
