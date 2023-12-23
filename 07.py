from functools import cmp_to_key

def parse_input():
    with open('input.txt') as input:
        hand_bid = {line.split()[0]: int(line.split()[1]) for line in input.readlines()}
    return hand_bid


def compare_by_card_value(hand_a, hand_b, is_part_two=False):
    for card_a, card_b in zip(hand_a, hand_b):
        a_value = get_card_value(card_a, is_part_two)
        b_value = get_card_value(card_b, is_part_two)
        if a_value > b_value:
            return 1
        if b_value > a_value:
            return -1
    return 0

def get_card_value(char, is_part_two=False):
    char_map = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 0 if is_part_two else 11,
        "T": 10
    }
    return int(char_map.get(char, char))

def get_comb_value(hand, is_part_two=False):
    unique_chars = set(hand)
    num_jokers = 0 if not is_part_two else hand.count('J')

    is_five_of_a_kind = len(unique_chars) == 1
    if is_five_of_a_kind:
        return 7

    is_four_of_a_kind = len(unique_chars) == 2 and hand.count(list(unique_chars)[0]) in [1,4]
    if is_four_of_a_kind:
        if num_jokers in [4,1]:
            return 7
        return 6

    is_full_house = len(unique_chars) == 2 and hand.count(list(unique_chars)[0]) in [3,2]
    if is_full_house:
        if num_jokers in [3,2]:
            return 7
        return 5

    is_three_of_a_kind = len(unique_chars) == 3 and any([hand.count(num) == 3 for num in unique_chars])
    if is_three_of_a_kind:
        if num_jokers in [1,3]:
            return 6
        if num_jokers == 2:
            return 7
        return 4

    is_two_pairs = len(unique_chars) == 3
    if is_two_pairs:
        if num_jokers == 2:
            return 6
        if num_jokers == 1:
            return 5
        return 3

    is_one_pair = len(unique_chars) == 4
    if is_one_pair:
        if num_jokers in [1,2]:
            return 4
        return 2
    return 2 if num_jokers == 1 else 1

def part_one_sort(hand_a, hand_b):
    comb_value_a = get_comb_value(hand_a)
    comb_value_b = get_comb_value(hand_b)
    if comb_value_a > comb_value_b:
        return 1
    elif comb_value_a == comb_value_b:
        return compare_by_card_value(hand_a, hand_b)
    return -1

def sort_func(hand_a, hand_b, is_part_two=False):
    comb_value_a = get_comb_value(hand_a, is_part_two)
    comb_value_b = get_comb_value(hand_b, is_part_two)
    if comb_value_a > comb_value_b:
        return 1
    elif comb_value_a == comb_value_b:
        return compare_by_card_value(hand_a, hand_b, is_part_two)
    return -1

def get_results(hand_bid):
    hands = list(hand_bid.keys())

    part_1 = 0
    hands.sort(key=cmp_to_key(sort_func))
    for mult, hand in enumerate(hands, start=1):
        part_1 += hand_bid[hand] * mult

    part_2 = 0
    hands.sort(key=cmp_to_key(lambda a,b: sort_func(a,b, True)))
    with open('output.txt', 'w') as f:
        for hand in hands:
            f.write(f'{hand}\n')
    for mult, hand in enumerate(hands, start=1):
        part_2 += hand_bid[hand] * mult
    return part_1, part_2



print(get_results(parse_input()))
