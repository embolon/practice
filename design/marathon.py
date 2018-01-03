#!/usr/bin/env python

class ListNode(object):
    def __init__(self, player, sensor, rank):
        self.player = player
        self.sensor = sensor
        self.rank = rank
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = ListNode(0, 0, 0)
        self.tail = ListNode(0, 0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        last = self.tail.prev
        last.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def updateRank(self, node):
        nd = self.head.next
        while nd != self.tail and nd != node:
            nd.rank += 1
            nd = nd.next

    def endRank(self):
        nd = self.tail.prev
        return nd.rank

class Marathon(object):
    def __init__(self, sensors, players):
        self.sensors = {}
        self.players = {}
        self.nsensor = sensors
        self.nplayer = players
        for p in range(players):
            self.players[p] = ListNode(p, sensors, p+1)
        for s in range(sensors):
            self.sensors[s] = DoubleLinkedList()
        # start point, add all players to the start point
        # smaller sensor id is closer to finish line
        self.sensors[sensors] = DoubleLinkedList()
        for p in range(players):
            self.sensors[sensors].append(self.players[p])

    def start(self):
        print('Marathon has started')
        print(
            '{0} players participants and {1} '
            'sensors along the way'.format(len(self.players),
                                           len(self.sensors)-1))

    def end(self):
        print('Marathon has ended')

    def event(self, player, sensor):
        # player passed sensor
        pn = self.players[player]
        prevSensor = pn.sensor
        self.sensors[prevSensor].updateRank(pn)
        self.sensors[prevSensor].remove(pn)
        pn.sensor = sensor
        pn.rank = self.sensors[sensor].endRank() + 1
        self.sensors[sensor].append(pn)

    def rank(self):
        # show runner's rank
        res = []
        for p in range(self.nplayer):
            res.append(self.players[p].rank)
        return res

    def getRank(self, player):
        return self.players[player].rank

    def top(self, k):
        # show top k runners
        res = []
        for s in range(self.nsensor+1):
            sensor = self.sensors[s]
            nd = sensor.head.next
            while nd != sensor.tail:
                res.append(nd.player)
                nd = nd.next
                if len(res) == k:
                    return res
        return res


if __name__ == '__main__':
    mar = Marathon(3, 5)
    mar.start()
    mar.event(4, 2)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.event(2, 2)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.event(4, 1)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.event(3, 2)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.event(1, 2)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.event(2, 1)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.event(0, 2)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.event(4, 0)
    top = mar.top(4)
    print('top player', top)
    rank = mar.rank()
    print('rank', rank)
    mar.end()
