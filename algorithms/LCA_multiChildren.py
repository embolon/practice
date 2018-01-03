#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []


def LCA(root, p, q):
    if not root:
        return None
    if root.val == p or root.val == q:
        return root.val
    res = []
    for kid in root.children:
        res.append(LCA(kid, p, q))
    # check none results
    l, r = None, None
    for re in res:
        if re:
            if not l:
                l = re
            else:
                r = re
    if l and r:
        return root.val
    else:
        return l or r

if __name__ == '__main__':
    business = TreeNode('business')
    Restaurant = TreeNode('Restaurant')
    HomeService = TreeNode('HomeService')
    Other = TreeNode('Other')
    Chinese = TreeNode('Chinese')
    Japanese = TreeNode('Japanese')
    RestCA = TreeNode('RestCA')
    RestCB = TreeNode('RestCB')
    RestJA = TreeNode('RestJA')
    Cleanning = TreeNode('Cleanning')
    business.children.append(Restaurant)
    business.children.append(HomeService)
    business.children.append(Other)
    HomeService.children.append(Cleanning)
    Restaurant.children.append(Chinese)
    Restaurant.children.append(Japanese)
    Chinese.children.append(RestCA)
    Chinese.children.append(RestCB)
    Japanese.children.append(RestJA)

    print LCA(business, 'RestCA', 'RestJA')
    print LCA(business, 'RestCA', 'RestCB')
    print LCA(business, 'RestCA', 'Cleanning')

