with open('input.txt') as input:
    lines = input.readlines()

def parse_input_to_dict(lines):
    input_dict = {}
    for line in lines:
        game, sets = line.split(': ')
        _, game_id = game.split(' ')
        sets = sets.split(';')

        input_dict[int(game_id)] = []
        for set in sets:
            cubes = [cube.strip().split() for cube in set.split(',')]
            cubes = {color: int(num) for num, color in cubes}
            input_dict[int(game_id)].append(cubes)
    return input_dict

def part_one(dict_of_games: dict[int, list[dict[str,int]]]):
    cubes_input = {
        'red':12,
        'green': 13,
        'blue': 14,
    }
    id_sum = 0
    for game_id, sets in dict_of_games.items():
        # Oh look this could be one pretty long list comprehension ...
        all_sets_possible = all(
            [all([cube_set.get(color,0) <= num for color, num in cubes_input.items()])
             for cube_set in sets]
        )
        if all_sets_possible:
            id_sum += game_id
    return id_sum

def part_two(dict_of_games: dict[int, list[dict[str,int]]]):
    # So basically set power = maximum of every color in all sets in one game multiplied together
    powers_sum = 0
    for sets in dict_of_games.values():
        power = 1
        for color in ['red', 'blue', 'green']:
            power *= max(set.get(color, 0) for set in sets)
        powers_sum += power
    return powers_sum

print(part_one(parse_input_to_dict(lines)))
print(part_two(parse_input_to_dict(lines)))