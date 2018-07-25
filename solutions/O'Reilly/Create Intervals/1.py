def is_interval(array, index, value=1):
    if (index - 1 < 0):
        return True

    return (int(array[index]) - int(array[index - 1]) == value)


def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    if not data:
        return []

    data = sorted(data)

    # string example: "1 2 3 4 5 Break 7 8 Break 12"
    data = tuple(map(str, data))
    string = " ".join([(data[i]) if is_interval(data, i) else ("Break " + data[i]) for i in range(len(data))])

    intervals = []

    for part in string.split("Break"):
        part = part.strip().split(" ")
        part = tuple(map(int, part))
        intervals.append((part[0], part[-1]))

    return intervals

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
