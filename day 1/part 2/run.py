
def find_frequency():
    with open("input/numbers.txt", "r") as f:
        numbers = [int(item.rstrip()) for item in f]

    current_frequency = 0
    past_frequencies = [0]
    while True:
        for item in numbers:
            current_frequency += item
            if current_frequency in past_frequencies:
                return current_frequency
            past_frequencies.append(current_frequency)
print(find_frequency())
