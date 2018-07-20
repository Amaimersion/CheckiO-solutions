def time_to_int(time):
    return list(map(int, time.split(":")))

def sun_angle(time):
    time = time_to_int(time)
    angle_in_minute = 360 / (24 * 60)
    angle = (time[0] * 60 * angle_in_minute) + (time[1] * angle_in_minute)
    angle -= 6 * 60 * angle_in_minute # the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees

    if (0 <= angle <= 180):
        return angle
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")