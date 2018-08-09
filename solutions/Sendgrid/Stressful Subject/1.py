import re

def is_stressful(text):
    """
    ^[A-Z\W]*$ - if the text is fully upper case. \W for non-word characters (punctuation marks, etc.)
    !{3,}$ - 3 or more of `!` at the end of the text.
    [hH][eElL\W\d]+[pP] - a word that starts with `h` or `H` and ends with `p` or `P`, 
                          between these two should be at least one of this characters: 
                          `e`, `E`, `l`, `L`, `\W` - any non word character, `\d` - any digit.
                          This principle is used for all "red" words.
    """
    return bool(re.search(r"(^[A-Z\W]*$|!{3,}$|[hH][eElL\W\d]+[pP]|[aA][sSaA\W\d]+[pP]|[uU][rRgGeEnN\W\d]+[tT])", text))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')