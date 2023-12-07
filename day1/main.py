def extract_inputs():
    inputs = []

    with open(r'E:\dev\AoC\2023\day1\input.txt') as fo:
        for line in fo:
            inputs.append(line.replace('\n', ''))

    return inputs

def parse_input(input):
    first_number = ''
    last_number = ''

    passed_values = ''

    for i in input:
        if i.isdigit():
            first_number = i
            break
        else:
            passed_values += i
            number = check_for_string_number(passed_values)
            if number != -1:
                first_number = number
                break
    
    passed_values = ''
    for i in reversed(input):
        if i.isdigit():
            last_number = i
            break
        else:
            passed_values = i + passed_values
            number = check_for_string_number(passed_values)
            if number != -1:
                last_number = number
                break
    
    return str(first_number), str(last_number)

def check_for_string_number(values):
    string_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for item in string_numbers:
        if item in values:
            return string_numbers.index(item) + 1
        
    return -1

def main():
    inputs = extract_inputs()

    calibration_values = []

    for input in inputs:
        numbers = parse_input(input)
        calibration_values.append(numbers[0] + numbers[1])

    total = 0
    for item in calibration_values:
        total += int(item)

    print(total)

if __name__ == '__main__': main()