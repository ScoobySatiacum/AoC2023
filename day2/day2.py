def extract_inputs():
    inputs = []

    with open(r'E:\dev\AoC\2023\day2\input.txt') as fo:
        for line in fo:
            inputs.append(line.replace('\n', ''))

    return inputs

def part_1(inputs):
    impossible_games = []
    possible_games = []

    for item in inputs:
        game, dice = item.split(':')
        sets = dice.split(';')

        valid_game = True

        for set in sets:
            if game not in impossible_games:
                colors = set.split(',')
                for color in colors:
                    if 'red' in color:
                        red_number = color.replace('red', '').strip()
                        if int(red_number) > 12:
                            impossible_games.append(game)
                            valid_game = False
                            break
                    if 'green' in color:
                        green_number = color.replace('green', '').strip()
                        if int(green_number) > 13:
                            impossible_games.append(game)
                            valid_game = False
                            break
                    if 'blue' in color:
                        blue_number = color.replace('blue', '').strip()
                        if int(blue_number) > 14:
                            impossible_games.append(game)
                            valid_game = False
                            break
        
        if valid_game:
            possible_games.append(game)

    return possible_games

def part_2(inputs):
    dice_powers = []

    for item in inputs:
        game, dice = item.split(':')
        sets = dice.split(';')

        min_red = None
        min_green = None
        min_blue = None

        for set in sets:
            colors = set.split(',')
            for color in colors:
                if 'red' in color:
                    if min_red is None:
                        min_red = int(color.replace('red', '').strip())
                    else:
                        num = int(color.replace('red', '').strip())
                        if num > min_red:
                            min_red = num
                if 'green' in color:
                    if min_green is None:
                        min_green = int(color.replace('green', '').strip())
                    else:
                        num = int(color.replace('green', '').strip())
                        if num > min_green:
                            min_green = num
                if 'blue' in color:
                    if min_blue is None:
                        min_blue = int(color.replace('blue', '').strip())
                    else:
                        num = int(color.replace('blue', '').strip())
                        if num > min_blue:
                            min_blue = num

        total = min_red * min_green * min_blue
        dice_powers.append(total)
    
    return sum(dice_powers)
                
def main():
    inputs = extract_inputs()
    #possible_games = part_1(inputs)

    #total = 0
    #for item in possible_games:
        #game, game_number = item.split(' ')
        #total += int(game_number)

    #print('Answer to part 1: ' + total)
    part_2_answer = part_2(inputs)
    print('Answer to part 2: ' + str(part_2_answer))

if __name__ == '__main__':
    main()