"""
Example: 
Output - [[0], [2], [0, 3], []]
"""
def get_cipher_indexes(cipher_grille):
    indexes = []

    for cipher in cipher_grille:
        indexes.append([i for i in range(len(cipher)) if cipher.startswith("X", i)])

    return indexes

"""
-> 90 degrees:
1 row -> 4 col
2 row -> 3 col
3 row -> 2 col
4 row -> 1 col

1 col -> 1 row
2 col -> 2 row
3 col -> 3 row 
4 col -> 4 row
"""
def turn_90(indexes, number):
    # 1 - we don't touch the initial position.
    for i in range(1, number + 1):
        indexes.append([])

        for index in indexes[i - 1]:
            row, col = index[1], abs(index[0] - 3)
            indexes[i].append([row, col])

    return indexes

"""
Example:
Input -  [[[0, 3], [2, 2], [0, 1], [3, 1]]]
Output - [[[0, 1], [0, 3], [2, 2], [3, 1]]]
"""
def sort(chars_indexes):
    for i in range(len(chars_indexes)):
        chars_indexes[i].sort(key=lambda i: (i[0], i[1]))

def recall_password(cipher_grille, ciphered_password):
    cipher_indexes = get_cipher_indexes(cipher_grille)
    chars_indexes = []

    # create initial.
    for i in range(1):
        chars_indexes.append([])

        for row in range(len(cipher_indexes)):
            for col in cipher_indexes[row]:
                chars_indexes[i].append([row, col])

    chars_indexes = turn_90(chars_indexes, 3)
    sort(chars_indexes)

    password = ""

    for i in chars_indexes:
        for x in i:
            password += ciphered_password[x[0]][x[1]]

    return password

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
