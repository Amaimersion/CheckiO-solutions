def isPositive(number):
    return 1 if number > 0 else -1

def _to_encrypt(from_char, to_char, text, delta):
    text = list(text)
    min_code = ord(from_char)
    max_code = ord(to_char)
    delta = abs(delta) % (max_code - min_code + 1) * isPositive(delta)

    for i in range(len(text)):
        current_code = ord(text[i])

        if not (min_code <= current_code <= max_code):
            continue

        current_code += delta

        if (current_code > max_code):
            current_code = min_code + (current_code % max_code - 1)
        elif (current_code < min_code):
            current_code = max_code - (min_code % current_code - 1)

        text[i] = chr(current_code)

    return "".join(text)

def to_encrypt(text, delta):
    # A-Z and a-z should be separately,
    # because between them exists 6 non-word symbols. 
    text = _to_encrypt("A", "Z", text, delta)
    text = _to_encrypt("a", "z", text, delta)
    
    return text

if __name__ == "__main__":
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    assert to_encrypt("hello", 36) == "rovvy", "Out of delta"
    assert to_encrypt("hello", -48) == "lipps", "Out of delta"
    assert to_encrypt("HeLLo in the RaBBit HoLe", 4) == "LiPPs mr xli VeFFmx LsPi", "Upper and lower case"
    print("Coding complete? Click 'Check' to earn cool rewards!")