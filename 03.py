with open('input.txt') as input:
    lines = [list(line.strip()) for line in input.readlines()]


def check_direction(lines, row, col):
    try:
        char = lines[row][col]
        return (char, (row, col)) if char != '.' and not char.isdigit() else None
    except IndexError:
        return None

def part_one(lines):
    num_sum = 0
    for row in range(len(lines)):
        partial_num_str = ""
        adjacent_to_symbol = False
        for col in range(len(lines[row])):
            char = lines[row][col]
            if not char.isdigit():
                if adjacent_to_symbol:
                    num_sum += int(partial_num_str)
                partial_num_str = ""
                adjacent_to_symbol = False
                continue
            # Is number, need to check for adjacent symbols
            if char.isdigit():
                partial_num_str += char
                if not adjacent_to_symbol:
                    adjacent_to_symbol = any([
                        check_direction(lines, row, col-1),
                        check_direction(lines, row, col+1),
                        check_direction(lines, row-1, col),
                        check_direction(lines, row+1, col),
                        check_direction(lines, row+1, col+1),
                        check_direction(lines, row-1, col-1),
                        check_direction(lines, row+1, col-1),
                        check_direction(lines, row-1, col+1),
                    ])
        # End of line
        if adjacent_to_symbol and partial_num_str:
            num_sum += int(partial_num_str)

    return num_sum


def part_two(lines):
    # Keys coordinates of '*' symbol, value is list of numbers
    gears_dict = {}
    for row in range(len(lines)):
        partial_num_str = ""
        adjacent_gears = set()
        for col in range(len(lines[row])):
            char = lines[row][col]
            if not char.isdigit():
                for coord in adjacent_gears:
                    gears_dict[coord] = gears_dict.get(coord, []) + [int(partial_num_str)]
                partial_num_str = ""
                adjacent_gears = set()
                continue
            # Is number, need to check for adjacent symbols and filter only for '*'
            if char.isdigit():
                partial_num_str += char
                adjacent_gears |= set(
                    map(
                        lambda symbol_coord: symbol_coord[1],
                        list(
                            filter(
                                lambda symbol_coord: symbol_coord is not None and symbol_coord[0] == '*',
                                [
                                    check_direction(lines, row, col-1),
                                    check_direction(lines, row, col+1),
                                    check_direction(lines, row-1, col),
                                    check_direction(lines, row+1, col),
                                    check_direction(lines, row+1, col+1),
                                    check_direction(lines, row-1, col-1),
                                    check_direction(lines, row+1, col-1),
                                    check_direction(lines, row-1, col+1),
                                ]
                            )
                        )
                    )
                )
        # End of line
        if adjacent_gears and partial_num_str:
            for coord in adjacent_gears:
                gears_dict[coord] = gears_dict.get(coord, []) + [int(partial_num_str)]
            partial_num_str = ""

    return sum(nums[0] * nums[1] for nums in gears_dict.values() if len(nums) == 2)

print(part_one(lines))
print(part_two(lines))
