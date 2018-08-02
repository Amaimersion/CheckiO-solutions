from typing import List
import math

def checkio(a: int, b: int, c: int) -> List[int]:
    is_valid = lambda a, b, c: (a < b + c) and (b < a + c) and (c < a + b)
    find_angle = lambda a, b, c: round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c))))

    if not is_valid(a, b, c):
        return [0, 0, 0]

    angle_a = find_angle(b, a, c)
    angle_b = find_angle(a, b, c)
    angle_c = 180 - (angle_a + angle_b)

    return sorted([angle_a, angle_b, angle_c])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
