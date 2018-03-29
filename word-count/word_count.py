import re

def word_count(phrase):
    mod_phrase = phrase.lower()
    words = re.findall(r"([a-z0-9\']+)", mod_phrase)

    print(words)

    word_count = {}

    for word in words:
        word = word.strip("'")

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
