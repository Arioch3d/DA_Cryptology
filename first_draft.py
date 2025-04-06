""" 
This may end up being mostly psuedo code- 
Just trying to wrap my head around the concepts
"""

"""
C = cypher
P = plain text character
K1 = multiplicative key
K2 = additive key
C = (P * K1 + K2) mod 26
P = ((C - K2)/K1) mod 26
"""

# Function to encrypt text using the Affine Cipher
# def affine_encrypt(text, a, b):
#     encrypted = ""
#     for char in text:
#         if char.isalpha():  # Process only alphabetic characters
#             char = char.lower()
#             # Convert the character to a number (a=0, b=1, ..., z=25)
#             char_num = ord(char) - ord('a')
#             # Apply the Affine Cipher formula: (a * x + b) % 26
#             encrypted_char = chr(((a * char_num + b) % 26) + ord('a'))
#             encrypted += encrypted_char
#         else:
#             encrypted += char  # Keep non-alphabetic characters as is
#     return encrypted
    
# text = "hello"
# a = 5
# b = 13
# encrypted_text = affine_encrypt(text, a, b)
# print(encrypted_text)



# # Function to decrypt text using the Affine Cipher
# def affine_decrypt(encrypted_text, a, b):
#     decrypted = ""
#     # Find modular inverse of 'a' (mod 26)
#     def mod_inverse(x, m):
#         for i in range(1, m):
#             if (x * i) % m == 1:
#                 return i
#         return None

#     a_inverse = mod_inverse(a, 26)
#     if a_inverse is None:
#         raise ValueError("Inverse of 'a' mod 26 does not exist.")

#     for char in encrypted_text:
#         if char.isalpha():
#             char = char.lower()
#             char_num = ord(char) - ord('a')
#             # Apply the decryption formula: a_inv * (x - b) % 26
#             decrypted_char = chr((a_inverse * (char_num - b) % 26) + ord('a'))
#             decrypted += decrypted_char
#         else:
#             decrypted += char
#     return decrypted

# encrypted_text = "whqqf"
# a = 5
# b = 13
# decrypted_text = affine_decrypt(text, a, b)
# print(decrypted_text)



import string

# Define the alphabet
ALPHABET = string.ascii_uppercase

def letter_to_index(letter):
    return ALPHABET.index(letter)

def index_to_letter(index):
    return ALPHABET[index]

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(plaintext, a, b):
    ciphertext = ""
    for letter in plaintext:
        if letter in ALPHABET:
            x = letter_to_index(letter)
            encrypted_index = (a * x + b) % len(ALPHABET)
            ciphertext += index_to_letter(encrypted_index)
        else:
            ciphertext += letter
    return ciphertext

def decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = mod_inverse(a, len(ALPHABET))
    if a_inv is None:
        return "Error: 'a' is not coprime to 26"
    for letter in ciphertext:
        if letter in ALPHABET:
            y = letter_to_index(letter)
            decrypted_index = (a_inv * (y - b)) % len(ALPHABET)
            plaintext += index_to_letter(decrypted_index)
        else:
            plaintext += letter
    return plaintext

# Example usage
plaintext = "HELLO WORLD"
a, b = 5, 13  # Key values

encrypted = encrypt(plaintext, a, b)
decrypted = decrypt(encrypted, a, b)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")













"""
Charles' code:
this is my encrypt code:
def encrypt_cipher(plaintext, key1, key2):
    text = plaintext
    ciphertext = ""
    for char in text:
        if char.isalpha():
            order = ord(char)
            if char.islower():
                order = order - 97
                order = ((order * key1) + key2) % 26
                order = order + 97
                new_char = chr(order)
                ciphertext = ciphertext + new_char
            if char.isupper():
                order = order - 65
                order = ((order * key1) + key2) % 26
                order = order + 65
                new_char = chr(order)
                ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
    return ciphertext

"""





























#from wikipedia:
#import string

# def affine(a: int, b: int, s: str) -> str:
#     #Prints a transposition table for an affine cipher.
#     D = dict(enumerate(string.ascii_lowercase, start=0))
#     E = {v: k for k, v in D.items()}
#     size = len(string.ascii_lowercase)
#     ret = ""
#     print(size)
#     for c in s:
#         N = E[c]
#         val = a * N + b
#         val = val % size
#         print(f"{c}({N}) -> {D[val]}({val})")
#         ret += D[val]
#     return ret

# affine(5, 13, "hello")

# input_word = "abc"
# letter_index_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
# letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# K1 = 5
# K2 = 13
# #cypher_index = (K1 * letter_index + K2) % 26

# letter_index = 0

# for letter in input_word:
#     letter_index = enumerate(letter_list)
#     print(letter_index)
    

#index enumerate


# print("Welcome to the affine cypher!")

# crypt_type = (input("Would you like to (1)encrypt or (2)decrypt a message?"))
# message = str(input("Please enter a message to encrypt:")).lower
# mult_key = input("Please enter a multiplicative key value (1-26):")
# add_key = input("Please enter an additive key value (1-26):")

# if crypt_type == "1":
#     print("Encrypting... please wait.")
#     encrypted_message = message[::-1]
#     print(encrypted_message)
# elif crypt_type == "2":
#     print("Decrypting... please wait.")
    
# else:
#     print("Please enter 1 or 2")

    
    
# start_code_Dict = {"a": 0, "b": 1, "c": 2, "d": 3}


# def encrypt(message):
#     if crypt_type == "1":
#         print("Encrypting... please wait.")
#     elif crypt_type == "2":
#         print("Decrypting... please wait.")
    
#     # for letter in message_letters:
#     #     encrypted_message = 
        
#     encrypted_message = message[::-1]
    
#     print(encrypted_message)
    
    
# encrypt(message)

