with open('input.txt') as input:
    lines = [list(line.strip()) for line in input.readlines()]


def check_direction(lines, row, col):
    try:
        char = lines[row][col]
        return char != '.' and not char.isdigit()
    except IndexError:
        return False

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
    return

print(part_one(lines))
# print(part_two(lines))
