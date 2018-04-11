from Node import *
import random
MAX_N = 20


def newHeight():
    h = 1
    while random.getrandbits(1) and h < MAX_N:
        h += 1
    return h


class SkipList:
    def __init__(self, *args):
        self.head = Node(None, MAX_N)
        self.tail = Node(None, MAX_N)
        for i in range(MAX_N):
            self.head.join(self.tail, i)

        if len(args) == 1:
            for x in args[0]:
                self.insert(x)

    def find(self, key):
        h = MAX_N - 1
        it = self.head
        while h >= 0:
            if it.adj[h] == self.tail or it.adj[h].key >= key:
                h -= 1
            else:
                it = it.adj[h]
        it = it.adj[0]
        if it == self.tail:
            return None
        else:
            return it

    def insert(self, key):
        newH = newHeight()
        newNode = Node(key, newH)
        it = self.head
        h = MAX_N - 1
        while h >= 0:
            if it.adj[h] == self.tail or it.adj[h].key >= key:
                if h < newH:
                    newNode.join(it.adj[h], h)
                    it.join(newNode, h)
                h -= 1
            else:
                it = it.adj[h]

    def erase(self, key):
        target = self.find(key)
        if target is None:
            print('No existe ese elemento')
            return
        h = MAX_N - 1
        it = self.head
        while h >= 0:
            if it.adj[h] == self.tail or it.adj[h].key > key:
                h -= 1
            elif it.adj[h] == target:
                it.join(target.adj[h], h)
                h -= 1
            else:
                it = it.adj[h]

    def __str__(self):
        st = 'SkipList: {\n'
        it = self.head.adj[0]
        while it != self.tail:
            st += '[' + str(it.key) + ', ' + str(len(it.adj)) + ']\n'
            it = it.adj[0]
        st += '\n}'
        return st

