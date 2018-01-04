def reverse(input=""):
    output = ""

    for i in range (len(input) - 1, -1, -1):
        output += input[i]
    
    return output
