def long_repeat(line):
    data = "".join(['1' if line[i] == line[i + 1] else '0' for i in range(len(line) - 1)])
    return (len(max(data.split('0'))) + 1 if data else 0)
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
