#!/usr/bin/env python

class heap():
    def __init__(self, data):
        self.data = data
        self.data.insert(0, len(data))

def min_heapify(v, pos):
    left = pos * 2
    right = pos * 2 + 1
    largest = left if left < v.data[0] and v.data[pos] > v.data[left] else pos
    largest = right if right < v.data[0] and v.data[largest] > v.data[right] else largest
    if largest != pos:
        v.data[largest], v.data[pos] = v.data[pos], v.data[largest]
        min_heapify(v, largest)

def max_heapify(v, pos):
    left = pos * 2
    right = pos * 2 + 1
    largest = left if left < v.data[0] and v.data[pos] < v.data[left] else pos
    largest = right if right < v.data[0] and v.data[largest] < v.data[right] else largest
    if largest != pos:
        v.data[largest], v.data[pos] = v.data[pos], v.data[largest]
        max_heapify(v, largest)

def build_heap(v, hp_func=max_heapify):
    last_root = (v.data[0] - 1) // 2
    for i in range(last_root, 0, -1):
        hp_func(v, i)

def heap_sort(v, hp_func=max_heapify):
    hv = heap(v)
    build_heap(hv, hp_func=hp_func)
    for i in range(len(hv.data), 1, -1):
        hv.data[1], hv.data[i] = hv.data[i], hv.data[1]
        hv.data[0] -= 1
        hp_func(hv, 1)
    return hv.data[1:]


if __name__ == '__main__':
    alist = [0,1,2,3,4,5,6,7,8,9]
    aheap = heap(alist)
    build_heap(aheap)
    print(aheap.data)
    blist = [9,8,7,6,5,4,3,2,1,0]
    bheap = heap(blist)
    build_heap(bheap, hp_func=min_heapify)
    print(bheap.data)
    clist = [0,5,1,6,2,7,3,8,4,9]
    nlist = heap_sort(clist)
    print(nlist)
