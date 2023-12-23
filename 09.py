
def parse_input():
    with open('input.txt') as input:
        lines = [list(map(int,line.split())) for line in input.readlines()]
    return lines

def extrapolate(report, is_part_two=False):
    total = 0
    for history in report:
        sequences = [history]
        while any(sequences[-1]):  # not all zeroes
            new_sequence = [
                sequences[-1][i + 1] - sequences[-1][i]
                for i in range(len(sequences[-1]) - 1)
            ]
            sequences.append(new_sequence)

        # go back and count the value
        for i in range(len(sequences)-2, -1, -1):
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
            if is_part_two:
                # prepend
                sequences[i] = [sequences[i][0] - sequences[i + 1][0], *sequences[i]]
            else:
                sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
        total += sequences[0][0 if is_part_two else -1]
    return total


print(extrapolate(parse_input()))
print(extrapolate(parse_input(), is_part_two=True))
