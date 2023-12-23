import math

def parse_input():
    with open('input.txt') as input:
        lines = input.readlines()
    directions = [0 if char == 'L' else 1 for char in lines[0].strip()]
    nodes = {}
    for line in lines[2:]:
        key, values = line.split(' = ')
        left, right = values[1:-2].split(', ')
        nodes[key] = (left, right)
    return directions, nodes

def part_one(directions, nodes):
    finish = 'ZZZ'
    current = 'AAA'
    step = 0
    while current != finish:
        if step == len(directions):
            directions += directions

        current = nodes[current][directions[step]]
        step += 1
    return step

def part_two(directions, nodes):
    starting_nodes = list(filter(lambda x: x[-1] == 'A', nodes.keys()))

    nodes_steps = []

    for current in starting_nodes:
        steps = 0
        if steps == len(directions):
            directions += directions

        while current[-1] != 'Z':
            if steps == len(directions):
                directions += directions

            current = nodes[current][directions[steps]]
            steps += 1
        nodes_steps.append(steps)
    return math.lcm(*nodes_steps)


directions, nodes = parse_input()
print(part_one(directions, nodes))
print(part_two(directions, nodes))
