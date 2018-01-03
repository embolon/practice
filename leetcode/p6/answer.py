#!/usr/bin/env python

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    rows = []
    for i in range(numRows):
        newRow = []
        if i == 0:
            start_multi = 0
            while True:
                idx = start_multi * (numRows - 1)
                if idx >= len(s):
                    break
                newRow.append(s[idx])
                start_multi += 2
        elif i == numRows - 1:
            start_multi = 1
            while True:
                idx = start_multi * (numRows - 1)
                if idx >= len(s):
                    break
                newRow.append(s[idx])
                start_multi += 2
        else:
            start_multi_1 = 0
            start_multi_2 = 2
            while True:
                idx1 = start_multi_1 * (numRows - 1) + i
                idx2 = start_multi_2 * (numRows - 1) - i
                if idx1 >= len(s):
                    break
                newRow.append(s[idx1])
                if idx2 >= len(s):
                    break
                newRow.append(s[idx2])
                start_multi_1 += 2
                start_multi_2 += 2
        rows += newRow
        print newRow
    return ''.join(rows)


a = convert('AB', 2)
print a
b = convert('abcdefg', 3)
print b
