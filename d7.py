wires = {}

start_rules = open("d7.txt").readlines()


def apply_rules(rules):
    global wires
    not_done = []
    for rule in rules:
        a, b = rule.strip().split(" -> ")
        try:
            if "NOT" in a:
                c, w = a.split(" ")
                v = wires[w] if w in wires else int(w)
                wires[b] = ~v
            elif " " in a:
                w1, c, w2 = a.split(" ")

                v1 = wires[w1] if w1 in wires else int(w1)
                v2 = wires[w2] if w2 in wires else int(w2)

                match c:
                    case "AND":
                        wires[b] = v1 & v2
                    case "OR":
                        wires[b] = v1 | v2
                    case "LSHIFT":
                        wires[b] = v1 << v2
                    case "RSHIFT":
                        wires[b] = v1 >> v2
            else:
                v = wires[a] if a in wires else int(a)
                wires[b] = v
        except:
            not_done.append(rule)

    return not_done


tmp_rules = start_rules[:]

while "a" not in wires:
    tmp_rules = apply_rules(tmp_rules)

a_val = wires["a"]
print(a_val)

wires = {}

start_rules.append(f"{a_val} -> b")

while "a" not in wires:
    start_rules = apply_rules(start_rules)

print(wires["a"])
