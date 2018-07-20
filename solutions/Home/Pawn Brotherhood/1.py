def safe_pawns(pawns):
    if not isinstance(pawns, list):
        pawns = list(pawns)

    pawns.sort(key=lambda x: ord(x[1]))
    safe_pawns = set()
    check = lambda x, y: abs(ord(x) - ord(y)) == 1

    for i in range(len(pawns)):
        current_pawn = pawns[i]

        for other_pawn in pawns[i + 1::]:
            if (check(current_pawn[0], other_pawn[0]) and 
                check(current_pawn[1], other_pawn[1])):
                    safe_pawns.add(other_pawn)

    return len(safe_pawns)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
