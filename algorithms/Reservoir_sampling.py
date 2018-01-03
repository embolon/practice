#!/usr/bin/env python

import random


def reservoirSampling(s, k):
    n = len(s)
    r = s[:k]

    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            r[j] = s[i]
    return r

if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(reservoirSampling(s, 3))
    print(reservoirSampling(s, 3))
    print(reservoirSampling(s, 3))
    print(reservoirSampling(s, 3))
    print(reservoirSampling(s, 3))
