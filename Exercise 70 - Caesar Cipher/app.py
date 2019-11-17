def input_int(msg: str):
    while True:
        try:
            return int(input(msg))
        except:
            print("Try again.")

def encode_char(char, first, shift):
    new_position = (ord(char) - ord(first) + shift) % 26 # alphabet
    new_char = chr(new_position + ord(first)) # unicode
    return new_char

def encode_string(string: str, shift):
    encoded_string = ""
    for char in string:
        new_char = char

        if char >= "a" and char <= "z":
            new_char = encode_char(char, "a", shift)

        elif char >= "A" and char <= "Z":
            new_char = encode_char(char, "A", shift)

        encoded_string += new_char

    return encoded_string

user_interested = True
while user_interested:
    message = input("Enter the message to encode: ")
    shift = input_int("Enter the encoding shift: ")
    encoded_message = encode_string(message, shift)

    print(f"The encoded message is {encoded_message}")
    user_interested = False if input("Do you want to encode more messages? [y/n]") == "n" else True