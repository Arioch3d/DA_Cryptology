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

#from wikipedia:
import string

def affine(a: int, b: int, s: str) -> str:
    #Prints a transposition table for an affine cipher.
    D = dict(enumerate(string.ascii_lowercase, start=0))
    E = {v: k for k, v in D.items()}
    size = len(string.ascii_lowercase)
    ret = ""
    print(size)
    for c in s:
        N = E[c]
        val = a * N + b
        val = val % size
        print(f"{c}({N}) -> {D[val]}({val})")
        ret += D[val]
    return ret

affine(5, 13, "foobar")

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

