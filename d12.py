import json

data = json.load(open("input/d12.txt"))


def recurse(d, ignore) -> int:
    t = 0
    elem = d.values() if type(d) is dict else d

    for v in elem:
        if type(v) is int:
            t += v
        elif type(v) is str:
            if ignore and v == "red" and type(d) is dict:
                return 0
        else:
            t += recurse(v, ignore)

    return t


print(recurse(data, False))
print(recurse(data, True))
