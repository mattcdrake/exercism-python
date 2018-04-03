import re

def hey(phrase):
    phrase = phrase.strip()
    if (len(phrase) <= 0):
        return "Fine. Be that way!"
    elif (re.search('[a-zA-Z]', phrase) and phrase.upper() == phrase and 
        phrase[-1] == "?"):
        return "Calm down, I know what I'm doing!"
    elif (phrase[-1] == "?"):
        return "Sure."
    elif (re.search('[a-zA-Z]', phrase) and phrase.upper() == phrase):
        return "Whoa, chill out!"
    return "Whatever."