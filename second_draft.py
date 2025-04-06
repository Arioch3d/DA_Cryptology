print("Welcome to the affine cypher.")

another_crypt = True
while True:
    crypt_choice = input("Would you like to (1)encrypt or (2)decrypt a message?")
    if crypt_choice == "1":
        plain_text = input("Please enter the message you would like to encrypt:").lower()

        chr(97)
        ord('a')
        alphabet_mapping = {chr(i):i-97 for i in range(97, 97+26)}
        alphabet_mapping_reverse = {i-97:chr(i) for i in range(97, 97+26)}

        mult_key = int(input("Please enter a multiplicative key (1-26):"))
        add_key = int(input("Please enter an additive key (1-16):"))
        key = [mult_key, add_key]
        print("Encrypting... please wait.\n-------------------------")

        [i for i in plain_text]
        plain_text_numbers = [alphabet_mapping[i] for i in plain_text]
        a, b = key
        cypher_text_numbers = [(a * i + b)% 26 for i in plain_text_numbers]
        cypher_text = [alphabet_mapping_reverse[i] for i in cypher_text_numbers]
        cypher_text = ''.join(cypher_text)
        print(f"Your encrypted message is: {cypher_text}")

    else:
        print("We don't have the code to decrypt yet.")
        
    another_crypt = input("Would you like to encrypt or decyrpt another message? (yes/no)").lower()
    if another_crypt == "no":
        another_crypt = False
        print("Thank you for using the affine cypher.")
        break
    elif another_crypt == "yes":
        continue
    else:
        print("Please enter yes or no.")
        