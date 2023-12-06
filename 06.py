def part_one():
    races = [
        (57, 291),
        (72, 1172),
        (69, 1176),
        (92, 2026),
    ]

    # races_test = [
    #     (7, 9),
    #     (15, 40),
    #     (30, 200)
    # ]

    result = 1
    for time, record_distance in races:
        count = 0
        for i in range(1, time):
            # speed * ( time - timeHoldingButton)
            distance = i * (time - i)
            if distance > record_distance:
                count += 1
            # I am sure there could be some mathematical opimization
        result *= count
    return result


def part_two():
    test_race = (71530, 940200)
    race = (57726992, 291117211762026)

    time, record_distance = race

    max_holding = None
    min_holding = None

    for i in range(time):
        distance = i * (time - i)
        if distance > record_distance:
            max_holding = i

    for i in range(time, 0, -1):
        distance = i * (time - i)
        if distance > record_distance:
            min_holding = i

    return (max_holding - min_holding) + 1


print(part_one())
print(part_two())
