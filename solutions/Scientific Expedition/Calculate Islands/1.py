def checkio(land_map):
    def get_neighbors(of_index):
        shift_row, shift_col = [(-1, 0, 1)] * 2

        for row in range(3):
            for col in range(3):
                current_row = abs(of_index[0] - shift_row[row])
                current_col = abs(of_index[1] - shift_col[col])
                value = None

                try: value = land_map[current_row][current_col]
                except Exception as e: continue # not in land_map

                if (value == 1):
                    yield (current_row, current_col)

    def get_all_neighbors(of_index):
        all_neighbors = []

        def get_all(index):
            for indx in get_neighbors(index):
                if indx not in all_neighbors:
                    all_neighbors.append(indx)
                    get_all(indx)

        get_all(of_index)

        return all_neighbors

    count = []
    checked = []

    for row in range(len(land_map)):
        for col in range(len(land_map[row])):
            value = land_map[row][col]
            index = (row, col)

            if ((value == 1) and (index not in checked)):
                neighbors = get_all_neighbors(index)
                checked.extend(neighbors)
                count.append(len(neighbors))

    return sorted(count)

if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    assert checkio([[1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1]]) == [24], "4rd example"