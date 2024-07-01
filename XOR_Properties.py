#!/usr/bin/env python3

import sys
# import this

from binascii import unhexlify

# Given hex strings
key1_hex = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2_xor_key1_hex = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2_xor_key3_hex = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag_xor_key1_key3_key2_hex = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

# Convert hex strings to bytes
key1 = unhexlify(key1_hex)
key2_xor_key1 = unhexlify(key2_xor_key1_hex)
key2_xor_key3 = unhexlify(key2_xor_key3_hex)
flag_xor_key1_key3_key2 = unhexlify(flag_xor_key1_key3_key2_hex)

# Calculate KEY2 using KEY2 ^ KEY1
key2 = bytes(a ^ b for a, b in zip(key1, key2_xor_key1))

# Calculate KEY3 using KEY2 ^ KEY3
key3 = bytes(a ^ b for a, b in zip(key2, key2_xor_key3))

# Calculate the flag using FLAG ^ KEY1 ^ KEY3 ^ KEY2
flag = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(flag_xor_key1_key3_key2, key1, key2, key3))

# Convert the flag to string
flag_str = flag.decode('ascii')

print(flag_str)
