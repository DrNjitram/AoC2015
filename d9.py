import itertools

locations = set()
routes = {}

for distance in open("d9.txt").readlines():
    cities, dist = distance.split(" = ")
    A, B = cities.split(" to ")

    locations.add(A)
    locations.add(B)

    routes[f"{A}-{B}"] = int(dist)
    routes[f"{B}-{A}"] = int(dist)

distances = []

for steps in itertools.permutations(locations):
    buffer = 0
    for i in range(len(steps)-1):
        buffer += routes[f"{steps[i]}-{steps[i+1]}"]
    distances.append(buffer)

print(min(distances))
print(max(distances))
