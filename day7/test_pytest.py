import pytest
from day7 import Part2
from collections import Counter

def test_part2_init():
    part2 = Part2(r'E:\dev\AoC2023\day7\input.txt')
    assert part2.input_location == r'E:\dev\AoC2023\day7\input.txt'

def test_part2_determine_hand_type_high_card():
    part2 = Part2(r'E:\dev\AoC2023\day7\input.txt')
    hand_types = part2.determine_hand_type()

    j_count = 0
    for item in hand_types['high_card']:
        if 'J' in list(item.keys())[0]:
            j_count += 1

    assert j_count == 0

def test_part2_determine_hand_type_one_pair():
    part2 = Part2(r'E:\dev\AoC2023\day7\input.txt')
    hand_types = part2.determine_hand_type()

    one_pair_examples = []

    for item in hand_types['one_pair']:
        if 'J' in list(item.keys())[0]:
            c = Counter(list(item.keys())[0])
            if len(c) < 5:
                one_pair_examples.append(item)

    assert len(one_pair_examples) == 0

def test_part2_determine_hand_type_two_pair():
    part2 = Part2(r'E:\dev\AoC2023\day7\input.txt')
    hand_types = part2.determine_hand_type()

    two_pair_examples = []

    for item in hand_types['two_pair']:
        if 'J' in list(item.keys())[0]:
            c = Counter(list(item.keys())[0])
            if c['J'] > 1:
                two_pair_examples.append(item)

    assert two_pair_examples