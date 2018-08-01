import calendar

def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    clndr = calendar.Calendar()
    count = [0, 0, 0, 0, 0, 0, 0]

    for i in range(1, 13):
        for day in clndr.itermonthdays2(year, i):
            if day[0]:
                count[day[1]] += 1

    return [day[1] for day in zip(count, calendar.day_name) if day[0] == max(count)]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
