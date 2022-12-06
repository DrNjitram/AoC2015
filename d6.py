from collections import defaultdict

lights = defaultdict(bool)
brightness = defaultdict(int)

for line in open("d6.txt").readlines():

    c, s, _, e = line.strip().replace("turn ", "").split(" ")

    sv, ev = zip([int(v) for v in s.split(",")], [int(v) for v in e.split(",")])

    for x in range(sv[0], sv[1] + 1):
        for y in range(ev[0], ev[1] + 1):
            match c:
                case "toggle":
                    brightness[(x, y)] += 2
                    if lights[(x, y)]:
                        lights[(x, y)] = False
                    else:
                        lights[(x, y)] = True
                case "off":
                    if brightness[(x, y)] > 0:
                        brightness[(x, y)] -= 1

                    lights[(x, y)] = False
                case "on":
                    brightness[(x, y)] += 1
                    lights[(x, y)] = True


print(sum(lights.values()))
print(sum(brightness.values()))
