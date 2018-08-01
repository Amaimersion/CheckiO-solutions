import calendar

def checkio(year):
    clndr = calendar.Calendar()
    count = 0

    for i in range(1, 13):
        for day in clndr.itermonthdays2(year, i):
            if (day == (13, 4)):
                count += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
