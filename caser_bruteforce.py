print("Please Input caser Encrypted Data for Decryption By brute force ")
encrypted_data = "YMNX NX FQUMF GWFAT HTSYFHYNSL YFSLT MTYJQ RNPJ"

encrypted_data_length = len(encrypted_data)
for k in range(1, 26):
    plain_text = []
    for i in range(encrypted_data_length):

        char = encrypted_data[i]
        order = ord(char)
        plain_text.append(chr(order - k))

    print(''.join(plain_text))
