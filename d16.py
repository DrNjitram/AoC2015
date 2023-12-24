aunts = [[pair.split(": ") for pair in line.strip().replace(": ", "-", 1).split("-")[1].split(", ")] for line in
         open("input/d16.txt").readlines()]

target = {
    "children": 3,
    "cats": 7,  # more
    "samoyeds": 2,
    "pomeranians": 3,  # fewer
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,  # fewer
    "trees": 3,  # more
    "cars": 2,
    "perfumes": 1
}

for i, aunt in enumerate(aunts):
    valid1 = True
    valid2 = True
    for item, val in aunt:
        if item in target:
            if int(val) != target[item]:
                valid1 = False

            if ((item in ["pomeranians", "goldfish"] and int(val) >= target[item])
                or (item in ["cats", "trees"] and int(val) <= target[item])) \
                    or (item not in ["pomeranians", "goldfish", "cats", "trees"] and int(val) != target[item]):
                valid2 = False

    if valid1: print(i + 1, "part 1")
    if valid2: print(i + 1, "Part 2")
