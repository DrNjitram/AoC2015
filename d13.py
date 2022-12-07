import itertools

people = set()
combo = {}
for line in open("d13.txt").readlines():
    A, val, B = line.replace(" happiness units by sitting next to ", ",").replace(" would ", ",").replace("lose ", "-").replace("gain ", "").strip()[:-1].split(",")

    people.add(A)

    combo[f"{A}-{B}"] = int(val)


for person in people:
    combo[f"{person}-You"] = 0
    combo[f"You-{person}"] = 0

people2 = people | {"You"}


seatings = []
for seating in itertools.permutations(people):
    feels = 0
    for i in range(len(seating)):
        feels += combo[f"{seating[i]}-{seating[i-1]}"]
        feels += combo[f"{seating[i-1]}-{seating[i]}"]
    seatings.append(feels)

print(max(seatings))

seatings = []
for seating in itertools.permutations(people2):
    feels = 0
    for i in range(len(seating)):
        feels += combo[f"{seating[i]}-{seating[i-1]}"]
        feels += combo[f"{seating[i-1]}-{seating[i]}"]
    seatings.append(feels)

print(max(seatings))