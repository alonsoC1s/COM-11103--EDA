class Node:
    def __init__(self, key, h):
        self.adj = [None] * h
        self.key = key

    def join(self, x, h):
        #print('Uní ' + str(self.key) + ' con ' + str(x.key) + ' at level ' + str(h))
        self.adj[h] = x
