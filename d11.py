import re

forbidden = ['i', 'o', 'l']

def inc(s: str) -> str:
    s = s[:-1] + chr(ord(s[-1]) + 1)
    while '{' in s:
        ind = s.rfind("{")
        s = s[:ind - 1] + chr(ord(s[ind - 1]) + 1) + "a" + s[ind + 1:]

    for c in forbidden:
        if c in s:
            ind = s.rfind(c)
            s = s[:ind] + chr(ord(s[ind]) + 1) + "a" * len(s[ind + 1:])
    return s



start = "vzbxkghb"
def get_next():
    global start
    while True:
        start = inc(start)
        if any([ord(start[i]) == ord(start[i+1])-1 == ord(start[i+2])-2 for i in range(0, len(start)-2)]) and len(re.findall(r'(\w)\1', start))>1:
            break
get_next()
print(start)
get_next()
print(start)