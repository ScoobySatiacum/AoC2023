def extract_inputs():
    inputs = []

    with open(r'E:\dev\AoC\2023\day4\input.txt') as fo:
        inputs = fo.read().splitlines()

    return inputs

def extract_numbers(numbers):
    winning_numbers, my_numbers = numbers.split(' | ')
    winning_numbers_list = winning_numbers.split(' ')
    my_numbers_list = my_numbers.split(' ')

    winning_numbers_list = [x for x in winning_numbers_list if x != '']
    my_numbers_list = [x for x in my_numbers_list if x != '']

    return winning_numbers_list, my_numbers_list

def part1(inputs):
    cards = {}
    total = 0
    for line in inputs:
        card, numbers = line.split(':')
        winning_numbers, my_numbers = numbers.split(' | ')
        winning_numbers_list = winning_numbers.split(' ')
        my_numbers_list = my_numbers.split(' ')

        winning_numbers_list = [x for x in winning_numbers_list if x != '']
        my_numbers_list = [x for x in my_numbers_list if x != '']

        score = 0

        for num in winning_numbers_list:
            if num in my_numbers_list:
                if score == 0:
                    score = 1
                else:
                    score = score * 2
        
        cards[card] = score
        total += score

    return total

def part2(inputs):
    cards = {}

    for line in inputs:
        card, numbers = line.split(':')
        if card.startswith('Card   '):
            card = card.replace('Card   ', 'Card ')
        elif card.startswith('Card  '):
            card = card.replace('Card  ', 'Card ')
        winning_numbers, my_numbers = extract_numbers(numbers)

        cards[card] = (winning_numbers, my_numbers)

    card_keys = list(cards.keys())

    tracking = {}
    copies = []

    for card in cards.keys():
        total_winners = 0
        winning_numbers, my_numbers = cards[card][0], cards[card][1]
    
        for num in winning_numbers:
            if num in my_numbers:
                total_winners += 1

        tracking[card] = total_winners

    # create a card counting dictionary and set each to one to
    # represent our initial collection
    card_counting = {}

    for card in card_keys:
        card_counting[card] = 1

    current_card = 2

    for card in card_keys:
        card_count = tracking[card]
        for i in range(card_counting[card]):
            for j in range(current_card, current_card + card_count):
                card_counting['Card ' + str(j)] += 1
        current_card += 1
    
    total = 0

    for card in card_counting.keys():
        total += card_counting[card]

    return total

def main():
    inputs = extract_inputs()
    print(part1(inputs))
    print(part2(inputs))
        

if __name__ == '__main__':
    main()