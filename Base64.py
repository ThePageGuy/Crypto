#!/usr/bin/env python3

import sys
# import this

import base64

# Given hex string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Decode the hex string into bytes
byte_data = bytes.fromhex(hex_string)

# Encode the bytes into Base64
base64_encoded = base64.b64encode(byte_data)

# Convert the Base64 bytes to a string
base64_string = base64_encoded.decode('ascii')

print(base64_string)
