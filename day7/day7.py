def extract_inputs():
    inputs = []
    with open(r'E:\dev\AoC2023\day7\input.txt') as fo:
        inputs = fo.read().splitlines()

    return inputs

def part1(inputs):
    hands = extract_hands(inputs)

    hand_types = determine_hand_type(hands)
    
    # determine hand strengths
    strengths = []
    for hand in hand_types['three_kind']:
        if strengths:
            for item in strengths:
                item
        else:
            strengths.append(hand)


def determine_hand_type(hands):
    hand_types = {
        'five_kind': [],
        'four_kind': [],
        'full_house': [],
        'three_kind': [],
        'two_pair': [],
        'one_pair': [],
        'high_card': []
    }

    for hand in hands.keys():
        bid = hands[hand]

        # determine hand type
        cards = {}
        for i in hand:
            if i in cards.keys():
                cards[i] += 1
            else:
                cards[i] = 1

        if len(cards.keys()) == 5:
            hand_types['high_card'].append({hand: bid})
        elif len(cards.keys()) == 4:
            hand_types['one_pair'].append({hand: bid})
        elif len(cards.keys()) == 3:
            if 3 in cards.values():
                hand_types['three_kind'].append({hand: bid})
            else:
                if 1 in cards.values():
                    hand_types['two_pair'].append({hand: bid})
        elif len(cards.keys()) == 2:
            if 3 in cards.values():
                hand_types['full_house'].append({hand: bid})
            elif 4 in cards.values():
                hand_types['four_kind'].append({hand: bid})
        else:
            hand_types['five_kind'].append({hand: bid})

    return hand_types

def extract_hands(inputs):
    hands = {}
    for line in inputs:
        hand, bid = line.split(' ')
        hands[hand] = bid

    return hands

def main():
    inputs = extract_inputs()
    part1(inputs)

if __name__ == '__main__': main()