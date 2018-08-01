FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

"""
Example:
    Input - decompose(204, 100)
    Output - {100: 2, 10: 0, 1: 4}
"""
def decompose(number, until=100):
    numbers = {}

    while until >= 1:
        numbers[until] = number // until
        number %= until
        until //= 10

    return numbers

def checkio(number):
    numbers = decompose(number)
    isSecondTen = lambda i: 10 < 10 * i[10] + i[1] <= 19
    string = ""

    string = "{0} {1} {2} {3} {4}".format(
        FIRST_TEN[numbers[100]], 
        HUNDRED if numbers[100] else "",
        SECOND_TEN[numbers[1]] if isSecondTen(numbers) else "",
        OTHER_TENS[numbers[10]] if (numbers[10] and not isSecondTen(numbers)) else "",
        FIRST_TEN[numbers[1]] if (numbers[1] and not isSecondTen(numbers)) else "",
    )

    return " ".join(string.split()) # remove multiple spaces.

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')