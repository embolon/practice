#!/usr/bin/env python

# a system takes transaction information
# return top K most traded company
# return a company's currentPrice, currentProfit
# return top K profit company
# return top K most frequently changed company
# return top K highest in history company and its top price

# use double linked list to maintain the top K

class ListNode(object):
    def __init__(self, name, price, volume):
        self.name = name
        self.price = price
        self.volume = volume
        self.next = None
        self.prev = None

# if stock number is too big
# we only need to maintain a linked list of size k (max k)
# we only maintain the position if the stock volume
# is bigger than the last one in the list.
class DoubleLinkedList(object):
    def __init__(self):
        self.head = ListNode(None, None, None)
        self.tail = ListNode(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        tailNode = self.tail.prev
        tailNode.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = tailNode

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node, prev):
        nextNode = prev.next
        prev.next = node
        node.next = nextNode
        nextNode.prev = node
        node.prev = prev

    def update(self, node, newVol):
        curr = node
        while (curr != self.head and
               newVol + node.volume > curr.volume):
            curr = curr.prev
        node.volume += newVol
        self.remove(node)
        self.insert(node, curr)

    def add(self, node):
        vol = node.volume
        curr = self.tail.prev
        while curr != self.head and vol > curr.volume:
            curr = curr.prev
        self.insert(node, curr)


class StockSystem(object):
    def __init__(self):
        self.stocks = {}
        self.dll = DoubleLinkedList()

    def update(self, name, price, volume):
        node = self.stocks[name]
        node.price = price
        self.dll.update(node, volume)

    def add(self, name, price, volume):
        node = ListNode(name, price, volume)
        self.stocks[name] = node
        self.dll.add(node)

    def topK(self, K):
        res = []
        node = self.dll.head.next
        while K and node != self.dll.tail:
            res.append(node)
            node = node.next
            K -= 1
        return res


if __name__ == '__main__':
    print('Hello stock')
    sys = StockSystem()
    # initiate all stocks
    sys.add('Apple', 1000, 300)
    sys.add('BB', 10, 20)
    sys.add('Cestco', 60, 20)
    sys.add('Iron Mountain', 60, 30)
    sys.add('Microsoft', 50, 20)
    # top 3 volume
    print('current tops')
    nodes = sys.topK(3)
    for nd in nodes:
        print(nd.name, nd.price, nd.volume)
    # update volumes and prices
    sys.update('Apple', 800, 20)
    sys.update('BB', 12, 200)
    print('current tops')
    nodes = sys.topK(2)
    for nd in nodes:
        print(nd.name, nd.price, nd.volume)

    # keep updading
    sys.update('Microsoft', 60, 20)
    sys.update('Iron Mountain', 100, 400)
    print('current tops')
    nodes = sys.topK(5)
    for nd in nodes:
        print(nd.name, nd.price, nd.volume)
