from collections import defaultdict


def get_neighbours(pos):
    nbs = []
    x, y = pos
    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [1, 0], [0, -1], [0, 1]]:
        nbs.append((x + dx, y + dy))
    return nbs


def print_gol(state: dict):
    print("Field:")
    x_s, y_s = zip(*list([k for k,v in state.items() if v]))
    for y in range(min(y_s), max(y_s) + 1):
        line = ""
        for x in range(min(x_s), max(x_s) + 1):
            line += "#" if state[(x, y)] else "."
        print(line)


def step(state: dict) -> dict:
    next_state = defaultdict(lambda: 0)
    neighbours = set()
    for k, v in state.items():
        if v:
            neigh = get_neighbours(k)
            neighbours.update(neigh)
            if 2 <= sum(state[l] for l in neigh) <= 3:
                next_state[k] = 1

    for k in neighbours:
        if sum(state[l] for l in get_neighbours(k)) == 3:
            next_state[k] = 1

    return next_state


prev_state = defaultdict(lambda: 0)

for y, line in enumerate(open("input/d18_test.txt").readlines()):
    for x, c in enumerate(line):
        if c == '#':
            prev_state[(x, y)] = 1

print_gol(prev_state)
next_state = step(prev_state)
print_gol(next_state)
