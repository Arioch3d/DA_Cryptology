
plain_text = input("Please enter the message you would like to encrypt:").lower()


chr(97)
ord('a')

alphabet_mapping = {chr(i):i-97 for i in range(97, 97+26)}
#print(english_alphabet_mapping)
alphabet_mapping_reverse = {i-97:chr(i) for i in range(97, 97+26)}
#print(english_alphabet_mapping_reverse)

key = [5,18]
#print(key)

#print(english_alphabet_mapping['a'])
[i for i in plain_text]

plain_text_numbers = [alphabet_mapping[i] for i in plain_text]
#print(plain_text_numbers)

a, b = key
#print(a, b)

# cypher_text_numbers = [a * i + b for i in plain_text_numbers]
# print(cypher_text_numbers)
# cypher_text_numbers = [i % 26 for i in cypher_text_numbers]
# print(cypher_text_numbers)
cypher_text_numbers = [(a * i + b)% 26 for i in plain_text_numbers]
#print(cypher_text_numbers)

cypher_text = [alphabet_mapping_reverse[i] for i in cypher_text_numbers]
#print(cypher_text)
#print(''.join(cypher_text))
cypher_text = ''.join(cypher_text)
print(cypher_text)



