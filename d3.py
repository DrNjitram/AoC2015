from collections import defaultdict

visits = defaultdict(int)
visits2 = defaultdict(int)
visits[(0, 0)] = 1
visits2[(0, 0)] = 1
s = [0, 0]
s2 = [0, 0]
moves = open("d3.txt").readline()

robo = False
for move in moves:
    if robo:
        robo = False
        match move:
            case "^":
                s[0] += 1

            case ">":
                s[1] += 1

            case "<":
                s[1] -= 1

            case "v":
                s[0] -= 1

        visits[tuple(s)] += 1
    else:
        robo = True
        match move:
            case "^":
                s2[0] += 1

            case ">":
                s2[1] += 1

            case "<":
                s2[1] -= 1

            case "v":
                s2[0] -= 1

        visits2[tuple(s2)] += 1


print(len(set(visits.keys()) | set(visits2.keys())))
#  2837 too high