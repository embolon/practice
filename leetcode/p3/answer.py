#!/usr/bin/env python

def lengthOfLongestSubstring(s):
    longest = 0
    cur = ''
    for c in s:
        if c in cur:
            len_cur = len(cur)
            if len_cur > longest:
                 print cur
                 longest = len_cur
            cur = cur[(cur.find(c)+1):] + c
            print "new cur", cur
        else:
            cur = cur + c
    len_cur = len(cur)
    print cur
    if len_cur > longest:
        longest = len_cur
    return longest

print 'abcabcdecdefgh'
a = lengthOfLongestSubstring('abcabcdecdefgh')
print a
