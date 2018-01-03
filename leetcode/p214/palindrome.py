#!/usr/bin/env python

def shortest(s):
    if not s or len(s) == 1:
        return s
    j = 0
    for i in reversed(range(len(s))):
        if s[i] == s[j]:
            j += 1
    print j, len(s)
    r0 = s[::-1][:len(s)-j]
    r1 = shortest(s[:j-len(s)])
    r2 = s[j-len(s):]
    print r0, r1, r2
    return r0+r1+r2


if __name__ == '__main__':
    s = 'aacecaaa'
    print(shortest(s))
