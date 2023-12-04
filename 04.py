with open('input.txt') as input:
    lines = input.readlines()

def parse_lines(lines):
    cards = {}
    for line in lines:
        winning, have = line.strip().split(' | ')
        card, winning = winning.split(': ')
        card = int(card.split(' ')[-1].strip())
        winning = winning.replace('  ', ' ')
        have = have.replace('  ', ' ')
        cards[card] = {
            'winning': [int(num) for num in winning.split(' ') if num != ''],
            'have': [int(num) for num in have.split(' ') if num != ''],
            'count': 1,
            'worth': 0
        }
    return cards

def part_one(cards):
    for card_info in cards.values():
        card_points = 0
        for have_num in card_info['have']:
            if have_num in card_info['winning']:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2
        card_info['worth'] = card_points
    return sum(card['worth'] for card in cards.values())


def part_two(cards):
    for card_id, info in cards.items():
        matching_nums = sum([1 for have_num in info['have'] if have_num in info['winning']])
        for _ in range(info['count']):
            for i in range(1, matching_nums+1):
                cards[card_id + i]['count'] += 1
    return sum(info['count'] for info in cards.values())

print(part_one(parse_lines(lines)))
print(part_two(parse_lines(lines)))
