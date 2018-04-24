alphabet = "abcdef"

def rotate(text, key):
    char_arr = []

    for char in text:
        char_arr.append(shift_char(char, key))
    
    return "".join(char_arr)

def shift_char(char, key):
    if not char.isalpha():
        return char
    elif char.isupper():
        return chr((((ord(char) - 65) + key) % 26) + 65)
    elif char.islower():
        return chr((((ord(char) - 97) + key) % 26) + 97)
