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

#z = encrypt_cipher()
def decrypt_cipher(ciphertext, key1, key2):
    text = ciphertext
    #ciphertext = ""
    for char in text:
        if char.isalpha():
            order = ord(char)
            if char.islower():
                order = order - 97
                order = ((order * key2) - key1) % 26
                order = order + 97
                new_char = chr(order)
                plaintext = text + new_char
            if char.isupper():
                order = order - 65
                order = ((order * key2) - key1) % 26
                order = order + 65
                new_char = chr(order)
                plaintext = text + new_char
        else:
            plaintext = text + char
    return plaintext

plaintext = input("Enter the plaintext: ")
user_multiplicative = int(input("Enter Multiplicative Key: "))
user_additive = int(input("Enter Additive Key: "))

decrypted_text = decrypt_cipher(ciphertext, user_multiplicative, user_additive)

print("Entered plaintext: ", plaintext)
print("Entered keys are: \n Multiplicative Key = ", user_multiplicative, "\n Additive Key = ", user_additive)
print("Ciphertext : ", ciphertext)
print("Decrypted text: ", decrypted_text)