vowels = "aeiou"
dissalowed = ["ab", "cd", "pq", "xy"]

lines = [l.strip() for l in open("d5.txt").readlines()]

nice = 0
nicer = 0
for line in lines:
    if sum([line.count(v) for v in vowels]) >= 3 and not any([s in line for s in dissalowed]) and any([line[i] == line[i + 1] for i in range(0, len(line) - 1)]):
        nice += 1

    if any([line[i+2:].count(line[i:i+2]) > 0 for i in range(0, len(line)-1)]) and any([line[i] == line[i + 2] for i in range(0, len(line)-2)]):
        nicer += 1

print(nice)
print(nicer)
