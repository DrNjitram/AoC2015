import itertools

containers = [int(v.strip()) for v in open("input/d17.txt").readlines()]
milk = 150

valid = 0
valid2 = 1
print(containers)
for i in range(len(containers)):
    for perm in itertools.combinations(containers, i):
        if sum(perm) == milk:
            valid += 1
    if valid > 0 and valid2:
        valid2 = 0
        print("Part 2:", valid)
print("Part 1:", valid)

