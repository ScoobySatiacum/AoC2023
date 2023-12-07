def extract_inputs():
    inputs = []
    with open(r'E:\dev\AoC\2023\day3\input.txt') as fo:
        for line in fo:
            inputs.append(line.replace('\n', ''))

    return inputs

def generate_number_map(inputs):
    numbers = {}
    # iterate rows
    for i in range(len(inputs)):
        # iterate chars in row, columns
        number = ''
        number_coords = []
        for j in range(len(inputs[i])):
            if inputs[i][j].isdigit():
                number += inputs[i][j]
                number_coords.append((i, j))
            elif inputs[i][j] == '.':
                if number != '':
                    # number has ended.
                    for coord in number_coords:
                        numbers[coord] = number
                    number = ''
                    number_coords = []
            else:
                if number != '':
                    # number has ended.
                    for coord in number_coords:
                        numbers[coord] = number
                    number = ''
                    number_coords = []
        if number != '':
            # number has ended.
            for coord in number_coords:
                numbers[coord] = number
            number = ''
            number_coords = []
    
    return numbers

def generate_part_map(inputs):
    parts = []

    for row in range(len(inputs)):
        for col in range(len(inputs[row])):
            if inputs[row][col].isdigit():
                pass
            elif inputs[row][col] == '.':
                pass
            else:
                parts.append((row, col))

    return parts

def part_1(inputs):
    numbers_map = generate_number_map(inputs)
    parts = generate_part_map(inputs)

    total = 0

    length = len(inputs) - 1

    for part in parts:
        # check north directions
        if part[0] >= 1:
            n_coord = (part[0] - 1, part[1])
            if n_coord in numbers_map.keys():
                total += int(numbers_map[n_coord])
            else:
                nw_coord = (part[0] - 1, part[1] - 1)
                ne_coord = (part[0] - 1, part[1] + 1)
                if nw_coord in numbers_map.keys():
                    total += int(numbers_map[nw_coord])
                if ne_coord in numbers_map.keys():
                    total += int(numbers_map[ne_coord])
        # check west
        w_coord = (part[0], part[1] - 1)
        if w_coord in numbers_map.keys():
            total += int(numbers_map[w_coord])
        # check east
        e_coord = (part[0], part[1] + 1)
        if e_coord in numbers_map.keys():
            total += int(numbers_map[e_coord])
        # check south directions
        if part[0] + 1 <= length:
            s_coord = (part[0] + 1, part[1])
            if s_coord in numbers_map.keys():
                total += int(numbers_map[s_coord])
            else:
                sw_coord = (part[0] + 1, part[1] - 1)
                se_coord = (part[0] + 1, part[1] + 1)
                if sw_coord in numbers_map.keys():
                    total += int(numbers_map[sw_coord])
                if se_coord in numbers_map.keys():
                    total += int(numbers_map[se_coord])

    return total

def part_2(inputs):
    numbers_map = generate_number_map(inputs)
    parts = generate_part_map(inputs)

    length = len(inputs) - 1

    total = 0

    for part in parts:
        if inputs[part[0]][part[1]] == '*':
            gear1 = None
            gear2 = None

            # check north directions
            if part[0] >= 1:
                n_coord = (part[0] - 1, part[1])
                if n_coord in numbers_map.keys():
                    if not gear1:
                        gear1 = numbers_map[n_coord]
                    elif not gear2:
                        gear2 = numbers_map[n_coord]
                    else:
                        continue
                else:
                    nw_coord = (part[0] - 1, part[1] - 1)
                    ne_coord = (part[0] - 1, part[1] + 1)
                    if nw_coord in numbers_map.keys():
                        if not gear1:
                            gear1 = numbers_map[nw_coord]
                        elif not gear2:
                            gear2 = numbers_map[nw_coord]
                        else:
                            continue
                    if ne_coord in numbers_map.keys():
                        if not gear1:
                            gear1 = numbers_map[ne_coord]
                        elif not gear2:
                            gear2 = numbers_map[ne_coord]
                        else:
                            continue
            # check west
            w_coord = (part[0], part[1] - 1)
            if w_coord in numbers_map.keys():
                if not gear1:
                    gear1 = numbers_map[w_coord]
                elif not gear2:
                    gear2 = numbers_map[w_coord]
                else:
                    continue
            # check east
            e_coord = (part[0], part[1] + 1)
            if e_coord in numbers_map.keys():
                if not gear1:
                    gear1 = numbers_map[e_coord]
                elif not gear2:
                    gear2 = numbers_map[e_coord]
                else:
                    continue
            # check south directions
            if part[0] + 1 <= length:
                s_coord = (part[0] + 1, part[1])
                if s_coord in numbers_map.keys():
                    if not gear1:
                        gear1 = numbers_map[s_coord]
                    elif not gear2:
                        gear2 = numbers_map[s_coord]
                    else:
                        continue
                else:
                    sw_coord = (part[0] + 1, part[1] - 1)
                    se_coord = (part[0] + 1, part[1] + 1)
                    if sw_coord in numbers_map.keys():
                        if not gear1:
                            gear1 = numbers_map[sw_coord]
                        elif not gear2:
                            gear2 = numbers_map[sw_coord]
                        else:
                            continue
                    if se_coord in numbers_map.keys():
                        if not gear1:
                            gear1 = numbers_map[se_coord]
                        elif not gear2:
                            gear2 = numbers_map[se_coord]
                        else:
                            continue

            if gear1 and gear2:
                gear_ratio = int(gear1) * int(gear2)
                total += gear_ratio

                gear1 = None
                gear2 = None

    return total

def main():
    inputs = extract_inputs()
    print(part_1(inputs))

    print(part_2(inputs))

if __name__ == '__main__':
    main()