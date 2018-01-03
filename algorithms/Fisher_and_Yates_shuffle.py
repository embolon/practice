#!/usr/bin/env python

import random


def shuffle(num):
    for i in range(len(num)-1):
        j = random.randint(i, len(num)-1)
        num[i], num[j] = num[j], num[i]


if __name__ == '__main__':
    num = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9]
    shuffle(num)
    print num
