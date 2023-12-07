def extract_inputs():
    inputs = []
    with open(r'E:\dev\AoC\2023\day5\input.txt') as fo:
        inputs = fo.read().splitlines()

    return inputs

def extract_seeds(seed_line):
    """Extracts seed numbers from the seeds line. Returns a list of seed numbers"""
    _, seeds = seed_line.split(': ')
    seed_numbers = seeds.split(' ')

    seed_numbers = list(map(int, seed_numbers))

    return seed_numbers

def extract_map(inputs, current_row):
    """Extracts the seed-to-soil map. This moves the line location 
    forward as well as parses the seed-to-soil map"""
    mappings = []

    max_length = len(inputs) - 1

    # first, extract all of the seed-to-soil maps
    line = inputs[current_row]
    while line != '':
        if current_row < max_length:
            current_row += 1
            line = inputs[current_row]
            if line != '':
                mapping = line.split(' ')
                mapping = list(map(int, mapping))
                mappings.append(mapping)
        else:
            line = ''

    return mappings

def location_from_seed(mappings, seed_numbers):

    if seed_numbers is list:
        source_numbers = seed_numbers

        for mapping in mappings.keys():
            source_numbers = execute_mapping(mappings[mapping], source_numbers)

        return source_numbers
    else:
        source_numbers = seed_numbers
        for mapping in mappings.keys():
            source_numbers = execute_mapping_part2(mappings[mapping], source_numbers)
        
        return source_numbers

def execute_mapping_part2(mapping, source_ranges):
    new_source_numbers = {}

    # extract the mapping ranges to validate against
    mapping_source_ranges = []
    mapping_dest_ranges = []

    for item in mapping:
        dest_range_start = item[0]
        source_range_start = item[1]
        range_length = item[2]

        dest_max_value = (dest_range_start + range_length) - 1
        source_max_value = (source_range_start + range_length) - 1

        mapping_source_ranges.append((source_range_start, source_max_value))
        mapping_dest_ranges.append((dest_range_start, dest_max_value))

    altered_keys = []

    for i in range(len(mapping_source_ranges)):
        mapping_source_min = mapping_source_ranges[i][0]
        mapping_source_max = mapping_source_ranges[i][1]

        for source_min in source_ranges.keys():
            source_max = source_ranges[source_min]

            # checking for:
            # [ source ]
            #      [ target ]
            if source_min not in altered_keys:
                if source_min <= mapping_source_min:
                    if source_max <= mapping_source_max:
                        if mapping_source_min <= source_max:
                            if mapping_source_max >= source_max:
                                off_set = mapping_dest_ranges[i][1] - mapping_source_max
                                new_source_numbers[source_min] = mapping_source_min - 1
                                new_source_numbers[mapping_source_min + off_set] = source_max + off_set
                                altered_keys.append(source_min)
                                continue

            # checking for:
            #      [ source ]
            # [ target ]
            if source_min not in altered_keys:
                if source_min >= mapping_source_min:
                    if source_max >= mapping_source_max:
                        if mapping_source_max >= source_min:
                            off_set = mapping_dest_ranges[i][1] - mapping_source_max
                            new_source_numbers[mapping_source_max] = source_max
                            new_source_numbers[source_min + off_set] = mapping_source_max + off_set
                            altered_keys.append(source_min)
                            continue

            # checking for:
            # [    source    ]
            #   [  target  ]
            if source_min not in altered_keys:
                if mapping_source_min >= source_min:
                    if mapping_source_max <= source_max:
                        off_set = mapping_dest_ranges[i][1] - mapping_source_max
                        new_source_numbers[source_min] = mapping_source_min - 1
                        new_source_numbers[mapping_source_min + off_set] = mapping_source_max + off_set
                        new_source_numbers[mapping_source_max + 1] = source_ranges[source_min]
                        altered_keys.append(source_min)
                        continue

            # checking for:
            #    [ source ]
            # [    target    ]
            if source_min not in altered_keys:
                if source_min >= mapping_source_min:
                    if source_max <= mapping_source_max:
                        off_set = mapping_dest_ranges[i][1] - mapping_source_max
                        new_source_numbers[source_min + off_set] = source_max + off_set
                        altered_keys.append(source_min)
                        continue

            new_source_numbers[source_min] = source_ranges[source_min]

    for key in altered_keys:
        if key in new_source_numbers.keys():
            del new_source_numbers[key]
        
    return new_source_numbers

def execute_mapping(mapping, source_numbers):
    new_source_numbers = []
    altered_numbers = []

    for item in mapping:
        dest_range_start = item[0]
        source_range_start = item[1]
        range_length = item[2]

        dest_max_value = (dest_range_start + range_length) - 1
        source_max_value = (source_range_start + range_length) - 1

        for num in source_numbers:
            if source_max_value >= num:
                if num >= source_range_start:
                    new_source_numbers.append(num + (dest_max_value - source_max_value))
                    altered_numbers.append(num)

    for item in source_numbers:
        if item not in altered_numbers:
            new_source_numbers.append(item)

    return new_source_numbers

def part1(inputs):
    seed_numbers = []

    mappings = {}

    for i in range(len(inputs)):
        if inputs[i].startswith('seeds'):
            seed_numbers = extract_seeds(inputs[i])
        elif inputs[i].startswith('seed-to-soil'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('soil-to-fertilizer'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('fertilizer'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('water'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('light'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('temperature'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('humidity'):
            mappings[inputs[i]] = extract_map(inputs, i)

    locations = location_from_seed(mappings, seed_numbers)

    minimum_location = min(locations)

    return minimum_location

def part2(inputs):
    seed_numbers = []

    mappings = {}

    for i in range(len(inputs)):
        if inputs[i].startswith('seeds'):
            seed_numbers = extract_seeds(inputs[i])
        elif inputs[i].startswith('seed-to-soil'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('soil-to-fertilizer'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('fertilizer'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('water'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('light'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('temperature'):
            mappings[inputs[i]] = extract_map(inputs, i)
        elif inputs[i].startswith('humidity'):
            mappings[inputs[i]] = extract_map(inputs, i)

    seed_range_info = {}

    for i in range(0, len(seed_numbers) - 1, 2):       
        start = seed_numbers[i]
        range_length = seed_numbers[i + 1]
        seed_range_info[start] = start + range_length

    location_from_seed(mappings, seed_range_info)


def main():
    inputs = extract_inputs()
    #print(part1(inputs))
    part2(inputs)

if __name__ == '__main__': main()