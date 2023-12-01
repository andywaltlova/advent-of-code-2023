
with open('01.txt') as input:
    lines = input.readlines()

def part_one(lines: list):
    numbers = [[char for char in line if char.isdigit()] for line in lines]
    num_sum = 0
    for numbers_on_line in numbers:
        if len(numbers_on_line) == 0:
            continue
        elif len(numbers_on_line) == 1:
            num_sum += int(numbers_on_line[0] * 2)
        else:
            num_sum += int(numbers_on_line[0] + numbers_on_line[-1])
    return num_sum

def part_two(lines):
    def replace_if_exists(string):
        digits_strings = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }
        for string_num, int_num in digits_strings.items():
            if string_num in string:
                return string_num, int_num
        return None

    def replace_string_number(line, backwards=False):
        partial_string = ""
        for char in line:
            # Just return line if digit found sooner than letter digit
            if char.isdigit():
                return line[::-1] if backwards else line

            # Check from start for first occurence of letter digit
            partial_string = char + partial_string if backwards else partial_string + char
            if (num := replace_if_exists(partial_string)) is not None:
                to_replace = num[0][::-1] if backwards else num[0]
                replaced = line.replace(to_replace, str(num[1]), 1)
                return replaced[::-1] if backwards else replaced

        return line[::-1] if backwards else line

    modified_lines = []
    for line in lines:
        line = replace_string_number(line)
        line = replace_string_number(line[::-1], backwards=True)
        modified_lines.append(line)

    return part_one(modified_lines)

print(part_one(lines))
print(part_two(lines))