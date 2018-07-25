def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if not line:
        return ""

    if (max(line) == min(line)):
        return line[0]

    max_repeat = ""

    for i in range(len(line)):
        current = ""

        for x in range(i, len(line)):
            char = line[x]

            if (char not in current):
                current += char
            else:
                break

        if (len(current) > len(max_repeat)):
            max_repeat = current

    return max_repeat

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
