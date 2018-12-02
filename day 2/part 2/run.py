import collections

def run():
    with open("input/strings.txt", "r") as f:
        strings = [item.rstrip() for item in f]

    double_count = 0
    tripple_count = 0
    match_found = False

    for compare_string in strings:
        for check_string in strings:
            diffrences = 0
            for i in range(len(compare_string)):
                if not compare_string[i] == check_string[i]:
                    diffrences += 1
                if diffrences > 1:
                    break

            if diffrences == 1:
                matches = []
                for i in range(len(compare_string)):
                    if compare_string[i] == check_string[i]:
                        matches.append(compare_string[i])
                return matches


print(run())
