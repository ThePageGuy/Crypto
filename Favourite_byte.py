#!/usr/bin/env python3

import sys
# import this

from binascii import unhexlify

# Given hex string
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert hex string to bytes
data = unhexlify(hex_string)

# Function to XOR data with a single byte key
def xor_with_single_byte(data, key):
    return bytes([b ^ key for b in data])

# Try all possible keys (0 to 255)
for key in range(256):
    decrypted = xor_with_single_byte(data, key)
    try:
        decrypted_text = decrypted.decode('ascii')
        if all(32 <= ord(char) <= 126 for char in decrypted_text):  # Check if the text is printable
            print(f"Key: {key}, Decrypted: {decrypted_text}")
    except UnicodeDecodeError:
        pass
