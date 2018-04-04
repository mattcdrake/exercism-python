def decode(string):
    outstr = []
    i = 0

    while i < len(string):
        tempint = ""

        while (i < len(string) - 1) and string[i].isdigit():
            tempint += string[i]
            i += 1

        char = string[i]

        if tempint:
            tempint = int(tempint)

            while tempint > 0:
                outstr.append(char)
                tempint -= 1
        else:
            outstr.append(char)
        i += 1
    
    return "".join(outstr)



def encode(string):
    outstr = []
    i = 0

    while i < len(string):
        char = string[i]
        start = i

        while (i < len(string) - 1) and string[i] == string[i + 1]:
            i += 1

        if (i - start) > 0:
            outstr.append(str(i + 1 - start))      
        outstr.append(char)
        i += 1

    return "".join(outstr)
