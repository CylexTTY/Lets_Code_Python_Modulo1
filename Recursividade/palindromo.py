def palindromeCheck(txt):
    txt = ''.join((txt.lower().split()))
    if len(txt) <= 1:
        return True

    if txt[0] == txt[-1]:
        return palindromeCheck(txt[1:len(txt)-1])

    return False
    
print(palindromeCheck('Race car'))
