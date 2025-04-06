import string

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

print("Welcome to the Affine Cypher!")

crypt_again = True
while True:
    crypt_choice = int(input("Would you like to (1)encrypt or (2)decrypt a message?"))
    if crypt_choice == 1:
        plaintext = str(input("Please type the message you would like encrypted:")).upper()
        a = int(input("Please choose a multiplicative value(1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):"))
        b = int(input("Please choose an additive value (1-26):"))
        cyphertext = encrypt(plaintext, a, b)
        print(f"Your encrypted message is '{cyphertext}'")
    elif crypt_choice == 2:
        cyphertext = str(input("Please enter the message to be decrypted:")).upper()
        a = int(input("Please choose a multiplicative value(1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):"))
        b = int(input("Please choose an additive value (1-26):"))
        plaintext = decrypt(cyphertext, a, b)
        print(f"Your decrypted message is: {plaintext}")
     
    
    crypt_again = input("Would you like to encrypt or decrypt another message? (yes/no)").lower()
    if crypt_again == "no":
        another_crypt = False
        print("Thank you for using the affine cypher.")
        break
    elif crypt_again == "yes":
        continue
    else:
        print("You didn't enter 'yes' or 'no'.  I don't know how to make this part loop, so feel free to restart the program. lol")
        break
    
