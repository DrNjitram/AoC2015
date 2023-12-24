total = 0
total2 = 0
for line in open("input/d8.txt").readlines():
    line = line.strip()
    sline = line[1:-1]

    while "\\\\" in sline:
        sline = sline.replace("\\\\", "-")

    while "\\\"" in sline:
        sline = sline.replace("\\\"", "\"")

    while "\\x" in sline:
        x_index = sline.index("\\x")
        sline = sline[:x_index] + chr(int(sline[x_index+2:x_index+4], 16)) + sline[x_index+4:]

    total += len(line)-len(sline)
    total2 += 2 + line.count("\\") + line.count("\"")

print(total, total2)




