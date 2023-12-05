def parse_input():
    with open('input.txt') as input:
        lines = input.read()
    parts = lines.split('\n\n')
    seeds = list(map(int, parts[0].split(': ')[1].split(' ')))
    maps = []
    for category in parts[1:]:
        ranges = category.split('\n')[1:]
        ranges = [list(map(int, line.split(' '))) for line in ranges]
        maps.append(ranges)
    return seeds, maps

def map_from_category(ranges, seed, inverted=False):
    for destination_range, source_range, range_len in ranges:
        if not inverted:
            if source_range <= seed < source_range+range_len:
                return destination_range + (seed - source_range)
        else:
            if destination_range <= seed < destination_range+range_len:
                return source_range + (seed - destination_range)
    return seed

def part_one(seeds, maps):
    locations = []
    for seed in seeds:
        transformed = seed
        for category in maps:
            transformed = map_from_category(category, transformed)
        locations.append(transformed)
    return min(locations)

def is_in_seed_ranges(seeds, seed):
    for x, y in zip(seeds[::2], seeds[1::2]):
        if x <= seed < x + y:
            return True
    return False

def part_two(seeds, maps):
    # Hmm eh, let's do it inverted and hope for the best?

    # I kinda semi-manually guessed the optimal start based on part1
    location = part_one(seeds, maps) // 25
    while True:
        transformed = location // 1  # just need value not reference

        for category in maps[::-1]:
            transformed = map_from_category(category, transformed, inverted=True)

        if is_in_seed_ranges(seeds, transformed):
            return location
        location += 1


print(part_one(*parse_input()))
print(part_two(*parse_input()))
