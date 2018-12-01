with open("input/numbers.txt", "r") as f:
    result = 0
    for item in f:
        result += int(item.rstrip())
    print(result)
