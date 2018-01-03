#!/usr/bin/env python

def countSmaller(nums):
    def sort(enum):
        print enum
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            print left, right
            print smaller
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller

if __name__ == '__main__':
    nums = [5,2,6,1]
    print(countSmaller(nums))
