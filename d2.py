def paper(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, l*h])

def ribbon(l, w, h):
    return l*w*h + min([2*l+2*w, 2*w + 2*h, 2*l+2*h])

print(sum([paper(*[int(s) for s in p.strip().split("x")]) for p in open("d2.txt").readlines()]))
print(sum([ribbon(*[int(s) for s in p.strip().split("x")]) for p in open("d2.txt").readlines()]))