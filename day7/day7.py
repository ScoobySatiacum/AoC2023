class Day7:

    def __init__(self, input_location):
        self.input_location = input_location
        self.inputs = self.extract_inputs()
        self.hands = self.extract_hands()

    def extract_inputs(self):
        inputs = []
        with open(self.input_location) as fo:
            inputs = fo.read().splitlines()

        return inputs

    def extract_hands(self):
        hands = {}
        for line in self.inputs:
            hand, bid = line.split(' ')
            hands[hand] = bid

        return hands

class Part1(Day7):
    def execute(self):

        hand_types = self.determine_hand_type()

        hand_types = self.determine_hand_strengths(hand_types)

        total = 0
        strength_rank = 1
        for key in hand_types.keys():
            for item in hand_types[key]:
                total += strength_rank * int(list(item.values())[0])
                strength_rank += 1

        return total
    
    def determine_hand_type(self):
        hand_types = {
            'high_card': [],
            'one_pair': [],
            'two_pair': [],
            'three_kind': [],
            'full_house': [],
            'four_kind': [],
            'five_kind': [],
        }

        for hand in self.hands.keys():
            bid = self.hands[hand]

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

    def determine_hand_strengths(self, hand_types):
        for key in hand_types.keys():
            if len(hand_types[key]) > 1:
                
                self.sort_hand(hand_types[key])

        return hand_types

    def sort_hand(self, current_hands):
        hand_strength_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

        for i in range(len(current_hands) - 1):
            for j in range(0, len(current_hands) - i - 1):
                l1 = list(current_hands[j].keys())[0]
                l2 = list(current_hands[j + 1].keys())[0]

                for k in range(len(l1)):
                    if l1[k] != l2[k]:
                        if hand_strength_ranks.index(l1[k]) > hand_strength_ranks.index(l2[k]):
                            current_hands[j], current_hands[j + 1] = current_hands[j + 1], current_hands[j]
                            break
                        else:
                            break

class Part2(Day7):
    def execute(self):
        hand_types = self.determine_hand_type()

        hand_types = self.determine_hand_strengths(hand_types)

        total = 0
        strength_rank = 1
        for key in hand_types.keys():
            for item in hand_types[key]:
                total += strength_rank * int(list(item.values())[0])
                strength_rank += 1

        return total
    
    def determine_hand_type(self):
        hand_types = {
            'high_card': [],
            'one_pair': [],
            'two_pair': [],
            'three_kind': [],
            'full_house': [],
            'four_kind': [],
            'five_kind': [],
        }

        for hand in self.hands.keys():
            bid = self.hands[hand]

            # determine hand type
            cards = {}
            for i in hand:
                if i in cards.keys():
                    cards[i] += 1
                else:
                    cards[i] = 1

            if 'J' in hand:
                if len(cards.keys()) == 5:
                    # high card originally
                    hand_types['one_pair'].append({hand: bid})
                elif len(cards.keys()) == 4:
                    # one-pair originally
                    hand_types['three_kind'].append({hand: bid})
                elif len(cards.keys()) == 3:
                    # three-kind originally
                    if 3 in cards.values():
                        hand_types['four_kind'].append({hand: bid})
                    else:
                        # two-pair originally
                        if 1 in cards.values():
                            if cards['J'] == 1:
                                hand_types['full_house'].append({hand: bid})
                            elif cards['J'] == 2:
                                hand_types['four_kind'].append({hand: bid})
                elif len(cards.keys()) == 2:
                    if 3 in cards.values():
                        hand_types['five_kind'].append({hand: bid})
                    elif 4 in cards.values():
                        hand_types['five_kind'].append({hand: bid})
                else:
                    hand_types['five_kind'].append({hand: bid})
            else:
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
    
    def determine_hand_strengths(self, hand_types):
        for key in hand_types.keys():
            if len(hand_types[key]) > 1:
                
                self.sort_hand(hand_types[key])

        return hand_types

    def sort_hand(self, current_hands):
        hand_strength_ranks = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

        for i in range(len(current_hands) - 1):
            for j in range(0, len(current_hands) - i - 1):
                l1 = list(current_hands[j].keys())[0]
                l2 = list(current_hands[j + 1].keys())[0]

                for k in range(len(l1)):
                    if l1[k] != l2[k]:
                        if hand_strength_ranks.index(l1[k]) > hand_strength_ranks.index(l2[k]):
                            current_hands[j], current_hands[j + 1] = current_hands[j + 1], current_hands[j]
                            break
                        else:
                            break

def main():
    part1 = Part1(r'E:\dev\AoC2023\day7\input.txt')
    print(part1.execute())
    part2 = Part2(r'E:\dev\AoC2023\day7\input.txt')
    print(part2.execute())

if __name__ == '__main__': main()