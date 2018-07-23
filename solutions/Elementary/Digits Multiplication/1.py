def checkio(number):
    num = 1

    for i in str(number):
        num *= int(i) if int(i) else 1

    return num

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
