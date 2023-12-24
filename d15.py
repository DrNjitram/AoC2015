import numpy as np

ing = []

for ingr in open("d15.txt").readlines():
    ing.append([int(s.split(" ")[-1]) for s in ingr.split(", ")])

ing_arr = np.array(ing)

def get_product(quant):
    global ing_arr
    sums = np.sum([[int(q)] for q in quant] * ing_arr, 0)
    sums[sums < 0] = 0
    return np.prod(sums[:-1]), sums[-1]


ans = 0
ans2 = 0
for a in range(0, 101):
    for b in range(0, 101):
        if a + b > 100: continue
        for c in range(0, 101):
            if a + b + c > 100: continue
            for d in range(0, 101):
                if a + b + c + d != 100: continue
                product, cal = get_product([a, b, c, d])

                ans = max(product, ans)
                if cal == 500:
                    ans2 = max(product, ans2)



print(ans)
print(ans2)

