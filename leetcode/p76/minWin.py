#!/usr/bin/env python
import collections

def minWindow(s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        print c, missing, need
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            print i, s[i], need[s[i]]
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]

if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    print(minWindow(s, t))
