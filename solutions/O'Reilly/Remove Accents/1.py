import unicodedata

def checkio(string, accents=[
    b"\xcc\x8b", 
    b"\xcc\x8f",
    b"\xcc\x8a", 
    b"\xcc\xae", 
    b"\xcc\x8c", 
    b"\xcc\x80", 
    b"\xcc\x81", 
    b"\xcc\x83", 
    b"\xcc\x87",
    b"\xcc\x89", 
    b"\xcc\x84", 
    b"\xcc\x82", 
    b"\xcc\x86", 
    b"\xcc\x88", 
    b"\xcc\x9b",
    b"\xcc\x91",
    b"\xcc\xb1",
    b"\xcc\xa3",
    b"\xcc\xa7",
    b"\xcc\xa8"
    ]):
    #return unicodedata.normalize("NFD", string).encode("utf-8").translate(None, b" ".join(accents)).decode("utf-8")
    string = unicodedata.normalize("NFD", string).encode("utf-8")

    for accent in accents:
        string = string.replace(accent, b"")

    return string.decode("utf-8")

if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
