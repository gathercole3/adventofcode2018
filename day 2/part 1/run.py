import collections


double_count = 0
tripple_count = 0

with open("input/strings.txt", "r") as f:
    for string in f:
        results = collections.Counter(string)
        double_check = False
        tripple_check = False

        for key in results.keys():
            if results[key] == 2 and not double_check:
                double_check = True
                double_count += 1
            if results[key] == 3 and not tripple_check:
                tripple_check = True
                tripple_count += 1


print(double_count * tripple_count)
