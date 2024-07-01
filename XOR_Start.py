#!/usr/bin/env python3

import sys
# import this

def xor_string(input_string, key):
    # Step 1: Convert each character to its ASCII value and XOR with the key
    xor_result = [chr(ord(char) ^ key) for char in input_string]
    
    # Step 2: Combine the resulting characters into a new string
    new_string = ''.join(xor_result)
    
    return new_string

# Given string
label = "label"

# XOR each character with the integer 13
new_string = xor_string(label, 13)

# Format the result as the flag
flag = f"crypto{{{new_string}}}"

print(flag)
