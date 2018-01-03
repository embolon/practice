#!/usr/bin/env python

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val


def levelorder(root):
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def findParents(root, target):
    def helper(root, target, path, res):
        if not root:
            return
        if root.val == target:
            res.append(path)
            return
        helper(root.left, target, path+[root.val], res)
        helper(root.right, target, path+[root.val], res)
    
    res = []
    helper(root, target, [], res)
    return res[0] if res else []


if __name__ == '__main__':
    nodes = {}
    strs = 'ABCDEFGHI'
    for c in strs:
        nodes[c] = Node(c)

    root = nodes['F']
    root.left = nodes['B']
    root.right = nodes['G']
    nodes['B'].left = nodes['A']
    nodes['B'].right = nodes['D']
    nodes['D'].left = nodes['C']
    nodes['D'].right = nodes['E']
    nodes['G'].right = nodes['I']
    nodes['I'].left = nodes['H']

    inorder(root)
    preorder(root)
    postorder(root)
    levelorder(root)
    res = findParents(root, 'A')
    print res
    res = findParents(root, 'E')
    print res
