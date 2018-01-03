#!/usr/bin/env python

class q2s():
    def __init__(self):
        self.aq = []
        self.bq = []

    def push(self, num):
        while self.bq:
            self.aq.append(self.bq.pop(0))
        self.aq.append(num)

    def pop(self):
        while len(self.aq) != 1:
            self.bq.append(self.aq.pop(0))
        res = self.aq.pop(0)
        self.aq, self.bq = self.bq, self.aq
        return res

class s2q():
    def __init__(self):
        self.ins = []
        self.ons = []

    def push(self, num):
        while self.ons:
            self.ins.append(self.ons.pop())
        self.ins.append(num)

    def pop(self):
        while self.ins:
            self.ons.append(self.ins.pop())
        return self.ons.pop()


if __name__ == '__main__':
    fs = q2s()
    fs.push(2)
    fs.push(3)
    fs.push(4)
    last = fs.pop()
    print last
    last = fs.pop()
    print last
    last = fs.pop()
    print last

    fq = s2q()
    fq.push(2)
    fq.push(3)
    fq.push(4)
    last = fq.pop()
    print last
    last = fq.pop()
    print last
    last = fq.pop()
    print last
