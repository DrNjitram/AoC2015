
def iterate(start: str) -> str:
    result = ""
    buffer = start[0]
    for chr in start[1:]:
        if chr != buffer[-1]:
            result += str(len(buffer)) + buffer[-1]
            buffer = chr
        else:
            buffer += chr
    return result + str(len(buffer)) + buffer[-1]

s = "1113222113"

for i in range(50):
    s = iterate(s)

    print(f"{i}: {len(s)}")