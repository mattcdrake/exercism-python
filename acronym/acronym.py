import re

def abbreviate(words):
    words_list = re.split('[^a-zA-Z]', words)
    words_list = filter(None, words_list)
    letters = []
    
    for word in words_list:
        if word[0].isalpha():
            letters.append(word[0].upper())
            
    return "".join(letters)
