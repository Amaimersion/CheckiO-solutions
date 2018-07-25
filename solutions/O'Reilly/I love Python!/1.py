def i_love_python():
    """
        Let's explain why do we love Python.
    """
    return "I love Python!"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"

def animation(counter, length):
    stage = counter % (length * 2 + 2)
    if stage < length + 1:
        left_spaces = stage
    else:
        left_spaces = length * 2 - 1 - stage
    return '[' + ' ' * left_spaces + '=' + ' ' * (length - left_spaces) + ']'

for i in range(100):
    sys.stdout.write('\b\b\b')
    sys.stdout.write(animation(i, 6))
    sys.stdout.flush()
    time.sleep(0.2)