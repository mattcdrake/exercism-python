import re

def verify(isbn):
    formattedString = re.sub('[^xX0-9]+', '', isbn)

    if (len(formattedString) != 10):
        return False

    multiplicand = 10
    sumDigits = 0

    for char in formattedString:
        if (multiplicand != 1 and (char == 'x' or char == 'X')):
            return False
        elif (multiplicand == 1 and (char == 'x' or char == 'X')):
            sumDigits += 10
        else:
            sumDigits += multiplicand * int(char)
        
        multiplicand -= 1
    
    return sumDigits % 11 == 0
