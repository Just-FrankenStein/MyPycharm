def pldm(s):
    c = 0
    l = len(s)
    for x in range(l):
        if s[x] == s[-(x + 1)]:
            c = c + 1
        else:
            return False
    if c == l:
        return True


h = input()

if pldm(h):
    print('true')
else:
    print('false')