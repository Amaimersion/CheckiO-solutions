# !/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(data):
    return True if (
        len(data) >= 10 and 
        any(i.isdigit() for i in data) and 
        any(i.islower() for i in data) and 
        any(i.isupper() for i in data)
    ) else False

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("A1213pokl") == False, "1st example"
    assert checkio("bAse730onE4") == True, "2nd example"
    assert checkio("asasasasasasasaas") == False, "3rd example"
    assert checkio("QWERTYqwerty") == False, "4th example"
    assert checkio("123456123456") == False, "5th example"
    assert checkio("QwErTy911poqqqq") == True, "6th example"
