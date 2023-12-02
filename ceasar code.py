message = input("Enter your massage: ")
message = message.lower()
offset = int(input("Enter offset: "))
encoded_message = ""

for char in message:
    if char.isalpha():
        offset_char = chr(((ord(char) - ord('a')) + offset) % 26 + ord('a'))
        encoded_message += offset_char
    else:
        encoded_message += char
print(encoded_message)




