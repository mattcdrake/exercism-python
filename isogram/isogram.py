def is_isogram(string):
    seen_chars = []

    for char in string:
        if (char.isalpha() and char.lower() in seen_chars):
            return False
        seen_chars.append(char.lower())

    return True