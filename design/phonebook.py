#!/usr/bin/env python

ALPHA = list('0123456789abcdefghijklmnopqrstuvwxyz')

class TrieNode(object):
    def __init__(self):
        # self.data can used to check if this node is complete
        self.ch = {}
        self.parent = None
        self.c = None
        self.data = None

    def firstChild(self):
        for c in ALPHA:
            if c in self.ch:
                return self.ch[c]
        return None

    def lastChild(self):
        for c in ALPHA[::-1]:
            if c in self.ch:
                return self.ch[c]
    
    def nextSib(self):
        if not self.parent:
            return None
        for c in ALPHA[ALPHA.index(self.c)+1:]:
            if c in self.parent.ch:
                return self.parent.ch[c]
        return None

    def prevSib(self):
        if not self.parent:
            return None
        for c in ALPHA[ALPHA.index(self.c)-1::-1]:
            if c in self.parent.ch:
                return self.parent.ch[c]
        return None

    def nextCompleteNode(self):
        if self.ch:
            node = self.firstChild()
            while not node.data:
                node = node.firstChild()
            return node

        if not self.parent:
            return None

        # find next sib
        node = self
        while node and not node.nextSib():
            node = node.parent
        if not node:
            return None
        node = node.nextSib()

        # find first child of this sib
        while not node.data:
            node = node.firstChild()
        return node

    def prevCompleteNode(self):
        if not self.parent:
            return None

        # find prev sib
        node = self
        while node and not node.prevSib():
            node = node.parent
        if not node:
            return None
        node = node.prevSib()

        # find last child of this sib
        while not node.data:
            node = node.lastChild()
        return node


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, name, number):
        node = self.root
        for c in name:
            if c not in node.ch:
                node.ch[c] = TrieNode()
                node.ch[c].parent = node
                node.ch[c].c = c
            node = node.ch[c]
        if not node.data:
            node.data = {}
            node.data['name'] = name
            node.data['number'] = []
        node.data['number'].append(number)
        return node

    def search(self, name):
        node = self.root
        for c in name:
            if c not in node.ch:
                return None
            node = node.ch[c]
        if not node.data:
            return None
        return node

    def autocomplete(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.ch:
                return None
            node = node.ch[c]
        while not node.data:
            node = node.firstChild()
        return node


class PhoneBook(object):
    def __init__(self):
        self.trie = Trie()
        self.yellowpage = {}

    def add(self, name, number):
        node = self.trie.add(name, number)
        self.yellowpage[number] = node

    def searchName(self, name):
        return self.trie.search(name).data['number']

    def searchNumber(self, number):
        if number in self.yellowpage:
            return self.yellowpage[number].data['name']

    def autocomplete(self, prefix):
        node = self.trie.autocomplete(prefix)
        return node.data

    def neighbor(self, name):
        res = [None, None]
        node = self.trie.search(name)
        pn = node.prevCompleteNode()
        nn = node.nextCompleteNode()
        if pn:
            res[0] = pn.data
        if nn:
            res[1] = nn.data
        return res


if __name__ == '__main__':
    print('Hello This is Phone Book')
    book = PhoneBook()
    book.add('john', '123456789')
    book.add('john', '987654321')
    book.add('abc', '2222')
    book.add('abcdef', '0000')
    book.add('abcdgh', '3333')
    book.add('abcghk', '1111')
    book.add('abd', '5555')
    print('All Inputs')
    print('john\t123456789\n'
          'john\t987654321\n'
          'abc\t2222\n'
          'abcdef\t0000\n'
          'abcdgh\t3333\n'
          'abcghk\t1111\n'
          'abd\t5555\n')
    print('search john', book.searchName('john'))
    print('search 0000', book.searchNumber('0000'))
    print('auto abcd', book.autocomplete('abcd'))
    print('neighbor abc', book.neighbor('abc'))
    print('neighbor abcdgh', book.neighbor('abcdgh'))
    print('neighbor abcghk', book.neighbor('abcghk'))
