def extract_inputs():
    inputs = []
    with open(r'E:\dev\AoC2023\day6\input.txt') as fo:
        inputs = fo.read().splitlines()

    return inputs

def part1(inputs):
    parsed_inputs = parse_inputs(inputs)

    race_times = calculate_races(parsed_inputs)

    total = 1
    for item in race_times:
        total = total * len(item)
    
    return total

def part2(inputs):
    time, distance = parse_input_2(inputs)

    race_runs = execute_run(time, distance)

    return len(race_runs)

def execute_run(time, distance):
    race_runs = []
    
    for i in range(time):
        mm_per_s = i
        travel_time = time
        travel_time = travel_time - i

        traveled_distance = mm_per_s * travel_time
        if traveled_distance > distance:
            race_runs.append(i)
    
    race_runs.sort()
    
    return race_runs
    

def parse_input_2(inputs):
    time = 0
    distance = 0
    for line in inputs:
        if line.startswith('Time'):
            _, temp = line.split(':')
            temp = temp.strip()
            temp = temp.replace(' ', '')
            time = int(temp)
        if line.startswith('Distance'):
            _, temp = line.split(':')
            temp = temp.strip()
            temp = temp.replace(' ', '')
            distance = int(temp)

    return time, distance

def calculate_races(parsed_inputs):
    race_times = []

    for key in parsed_inputs.keys():
        race_runs = []

        distnace_to_beat = parsed_inputs[key]

        for i in range(key):
            mm_per_s = i
            time = key - i

            traveled_distance = mm_per_s * time
            if traveled_distance > distnace_to_beat:
                race_runs.append(traveled_distance)

        race_times.append(race_runs)

    return race_times


def parse_inputs(inputs):
    times = []
    distance = []
    for line in inputs:
        if line.startswith('Time'):
            _, temp = line.split(':')
            temp = temp.strip()
            temp_times = temp.split(' ')
            times = [int(x.strip()) for x in temp_times if x != '']
        if line.startswith('Distance'):
            _, temp = line.split(':')
            temp = temp.strip()
            temp_distances = temp.split(' ')
            distance = [int(x.strip()) for x in temp_distances if x != '']

    return dict(zip(times, distance))



def main():
    inputs = extract_inputs()
    print(part1(inputs))
    print(part2(inputs))

if __name__ == '__main__':
    main()