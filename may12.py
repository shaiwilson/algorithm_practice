
def compress(theStr):
    """ implement a method to perform basic string compression """ 

    outstring = []
    lastChar = ""
    charCount = 0
    for char in theStr:

        if char == lastChar:
            charCount += 1
        else:
            if lastChar != "":
                outstring.append(lastChar + str(charCount))
            charCount = 1
        lastChar = char