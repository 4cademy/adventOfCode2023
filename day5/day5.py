def load_data():
    data = []
    with open('maps') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


def get_seeds(data):
    seeds = []
    seed_line = data[0].split(':')[1]
    seeds = seed_line.split(' ')
    seeds = [seed for seed in seeds if seed != '']
    seeds = [int(seed) for seed in seeds]
    return seeds


def get_ranged_seeds(data):
    seeds = []
    seed_line = data[0].split(':')[1]
    seeds = seed_line.split(' ')
    seeds = [seed for seed in seeds if seed != '']
    seeds = [int(seed) for seed in seeds]

    ranged_seeds = []
    for i in range(0, len(seeds), 2):
        ranged_seeds.append([seeds[i], seeds[i]+seeds[i+1]-1])

    return ranged_seeds


def get_section(data, section):
    seed_to_soil = []
    try:
        start_index = data.index(f'{section} map:') + 1
    except ValueError:
        raise ValueError(f'No "{section}" map found in data')

    while start_index < len(data) and data[start_index] != '':
        line = data[start_index].split(' ')
        line = [int(num) for num in line]
        seed_to_soil.append(line)
        start_index += 1

    return seed_to_soil


def get_mapped_output(data, input_data, section_name):
    mapped_soil = []
    seed_to_soil = get_section(data, section_name)

    for num in input_data:
        mapped = False
        for line in seed_to_soil:
            if line[1] <= num <= (line[1] + line[2]):
                mapped_soil.append(line[0] + (num - line[1]))
                mapped = True
                break
        if not mapped:
            mapped_soil.append(num)

    return mapped_soil


def get_mapped_output_ranged(data, input_data, section_name):
    mapped_soil = []
    seed_to_soil = get_section(data, section_name)

    while input_data:
        pair = input_data.pop(0)
        mapped = False
        for line in seed_to_soil:
            start_out = line[0]
            start_in = line[1]
            end = line[1] + line[2] - 1
            if pair[0] < start_in <= pair[1] <= end:
                mapped_soil.append([start_out, start_out+(pair[1]-start_in)])
                input_data.append([pair[0], start_in-1])
                mapped = True
                break
            elif start_in <= pair[0] <= pair[1] <= end:
                mapped_soil.append([start_out+(pair[0]-start_in), start_out+(pair[1]-start_in)])
                mapped = True
                break
            elif start_in <= pair[0] <= end < pair[1]:
                mapped_soil.append([start_out+(pair[0]-start_in), start_out+(end-start_in)])
                input_data.append([end+1, pair[1]])
                mapped = True
                break

        if not mapped:
            mapped_soil.append(pair)

    return mapped_soil


def main():
    data = load_data()

    print(get_ranged_seeds(data))

    mapped_soil = get_mapped_output_ranged(data, get_ranged_seeds(data), 'seed-to-soil')
    print(mapped_soil)
    mapped_fertilizer = get_mapped_output_ranged(data, mapped_soil, 'soil-to-fertilizer')
    print(mapped_fertilizer)
    mapped_water = get_mapped_output_ranged(data, mapped_fertilizer, 'fertilizer-to-water')
    print(mapped_water)
    mapped_light = get_mapped_output_ranged(data, mapped_water, 'water-to-light')
    print(mapped_light)
    mapped_temperature = get_mapped_output_ranged(data, mapped_light, 'light-to-temperature')
    print(mapped_temperature)
    mapped_humidity = get_mapped_output_ranged(data, mapped_temperature, 'temperature-to-humidity')
    print(mapped_humidity)
    mapped_location = get_mapped_output_ranged(data, mapped_humidity, 'humidity-to-location')
    print(mapped_location)
    print(min([pair[0] for pair in mapped_location]))


if __name__ == '__main__':
    main()
