def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence_dict = {}

    for char in sentence:
        if char.lower() not in sentence_dict:
            sentence_dict[char.lower()] = 1
    
    for char in alphabet:
        if not char in sentence_dict:
            return False
    
    return True