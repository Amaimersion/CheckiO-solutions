def checkio(game_result):
    field_x = [[], [], []]
    field_o = [[], [], []]

    for row in range(3):
        for index in range(3):
            if game_result[row][index] == 'X':
                field_x[row].append(index)
            elif game_result[row][index] == 'O':
                field_o[row].append(index)

    check_1 = lambda x: any(((index in x[0] and index in x[1] and index in x[2]) or (len(x[index]) == 3)) for index in range(3))
    check_2 = lambda x: (1 in x[1]) and ((0 in x[0] and 2 in x[2]) or (2 in x[0] and 0 in x[2]))

    if check_1(field_x) or check_2(field_x): 
        return 'X'
    elif check_1(field_o) or check_2(field_o): 
        return 'O'
    else: 
        return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
