#!/usr/bin/env python

class TrieNode():
    def __init__(self):
        self.nodes = {}
        self.isword = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = TrieNode()
            cur = cur.nodes[c]
        cur.isword = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        return cur.isword

    def startWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        return True

if __name__ == '__main__':
    wordDict = Trie()
    wordDict.insert('dictionary')
    wordDict.insert('abcd')
    wordDict.insert('demo')
    print 'a', wordDict.search('a')
    print 'demo', wordDict.search('demo')
    print 'dict', wordDict.startWith('dict')
    print 'c', wordDict.startWith('c')
