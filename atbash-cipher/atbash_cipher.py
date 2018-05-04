def encode(plain_text):
    plain_text = plain_text.lower()
    out_text = []
    counter = 0

    for char in plain_text:
        if char.isalpha():
            out_text.append(chr(122 - (ord(char) - 97)))
            counter += 1
        elif char.isdigit():
            out_text.append(char)
            counter += 1
        if counter == 5:
            out_text.append(" ")
            counter = 0
        
    return "".join(out_text).strip()


def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    out_text = []

    for char in ciphered_text:
        if char.isalpha():
            out_text.append(chr(122 - (ord(char) - 97)))
        elif char.isdigit():
            out_text.append(char)
    
    return "".join(out_text)

