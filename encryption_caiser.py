plain_data = input("please input you plain Text for Encryption A-Z :")
key = input("Please input encryption Key: ")
encrypted_data = []
for i in range(len(plain_data)):
    char = plain_data[i]
    order = ord(char)
    encrypted_data.append(chr(order +int(key)))

print(''.join(encrypted_data))
