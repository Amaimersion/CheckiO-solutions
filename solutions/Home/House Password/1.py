# !/usr/bin/python
# -*- coding: utf-8 -*-

import re

def checkio(data):
    """
    ^ - not necessary with match(). The start of the string.
    (?=.*[0-9]) - at least one digit exists.
    (?=.*[A-Z]) - at least one upper case letter exists.
    (?=.*[a-z]) - at least one upper case lower exists.
    (?=\\w{10}) - the length is minimum 10.
    \\w+ - apply to the entire string and to the only ASCII characters
    $ - the end of the string.
    flags=re.A - is necessary for ASCII checking.    
    """
    return bool(re.match(r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=\w{10})\w+$", data, flags=re.A))

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("A1213pokl") == False, "1st example"
    assert checkio("bAse730onE4") == True, "2nd example"
    assert checkio("asasasasasasasaas") == False, "3rd example"
    assert checkio("QWERTYqwerty") == False, "4th example"
    assert checkio("123456123456") == False, "5th example"
    assert checkio("QwErTy911poqqqq") == True, "6th example"
    assert checkio("QwErTy911poqqqqпривет") == False, "7th example, only ASCII"