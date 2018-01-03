#!/usr/bin/env python

def findNth(n):
    start, size, step = 1, 1, 9
    while n > size * step:
        n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
    print n, size, step, start
    res = int(str(start + (n-1)/size)[(n-1)%size])
    return res

if __name__ == '__main__':
    print findNth(11)
    print findNth(20)
    print findNth(20000)
