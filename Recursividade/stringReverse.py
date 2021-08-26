def strRev(txt):
    return strRev(txt[1:]) + txt[0] if len(txt) > 1 else txt

print(strRev('String Reverse test case'))
