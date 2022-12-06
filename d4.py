import hashlib

i = 0
z = "0"
while True:
    h = "ckczppom" + str(i)
    if hashlib.md5(h.encode()).hexdigest().startswith(z):
        print(f"{len(z)}: {i}")
        z += "0"
        if len(z) > 6:
            break
    i += 1

