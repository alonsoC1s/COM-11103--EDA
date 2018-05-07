import queue
import networkx

class HashNode:
    def __init__(self, key):
        self.dato = key
        self.next = None


class HashTable:
    def __init__(self):
        self.arr = [None]
        self.cnt = 0

    def resize(self):
        newArr = [None] * (len(self.arr) * 2)

        for head in self.arr:
            it = head
            while it is not None:
                sig = it.next
                pos = hash(it.dato) % len(newArr)
                it.next = newArr[pos]
                newArr[pos] = it
                it = sig
        self.arr = newArr

    def insert(self, key):
        if self.cnt == len(self.arr):
            self.resize()
        pos = hash(key) % len(self.arr)
        newNode = HashNode(key)
        newNode.next = self.arr[pos]
        self.arr[pos] = newNode
        self.cnt += 1

    def find(self, key):
        pos = hash(key) % len(self.arr)
        if self.arr[pos] is None:
            return False
        else:
            it = self.arr[pos]
            while it is not None and it.dato != key:
                it = it.next
            if it is not None:
                return True
            else:
                return False

    def erase(self, key):
        pos = hash(key) % len(self.arr)
        if self.arr[pos] is None:
            print("Error. No existe esa llave")
        elif self.arr[pos].dato == key:
            self.arr[pos] = self.arr[pos].next
        else:
            it = self.arr[pos]
            while it.next is not None and it.next.dato != key:
                it = it.next
            if it.next.dato == key:
                it.next = it.next.next
                self.cnt -= 1
            else:
                print("Error. No existe esa llave");

    def __str__(self):
        res = ''
        for list in self.arr:
            res += '{'
            it = list
            while it is not None:
                res += str(it.dato) + ','
                it = it.next
            res += '}\n'
        return res


class grafo:
    def __init__(self):
        self.adj = {}
        self.num_vertices = 0

    def __str__(self):
        return str(self.adj)

    def __insertEdge__(self, u, v):
        if u not in self.adj.keys():
            self.adj[u] = []
            self.num_vertices += 1
        self.adj[u] += [v]

    def insertEdge(self, u, v):
        self.__insertEdge__(u, v)
        self.__insertEdge__(v, u)

    def dfs(self, nodo):
        iterador = []
        stack = [nodo]
        visitados = HashTable()
        while len(stack) > 0:
            nodo = stack.pop()
            if visitados.find(nodo) is False:
                visitados.insert(nodo)
                iterador += [nodo]
                for adj in self.adj[nodo]:
                    stack += [adj]
        return iterador

    def bfs(self, nodo):
        iterador = []
        q = queue.Queue()
        q.put(nodo)
        visitados = HashTable()
        while q.empty() is False:
            nodo = q.get()
            if visitados.find(nodo) is False:
                visitados.insert(nodo)
                iterador += [nodo]
                for adj in self.adj[nodo]:
                    q.put(adj)
        return iterador

g = grafo()
g.insertEdge('a', 'b')
g.insertEdge('a', 'h')
g.insertEdge('h', 'b')
g.insertEdge('h', 'i')
g.insertEdge('h', 'g')
g.insertEdge('i', 'c')
g.insertEdge('b', 'c')
g.insertEdge('d', 'c')
g.insertEdge('g', 'f')
g.insertEdge('f', 'c')
g.insertEdge('d', 'f')
g.insertEdge('e', 'f')
g.insertEdge('e', 'd')

networkx.draw(networkx.from_dict_of_lists(g.adj))
print(g.dfs('a'))
print(g.bfs('a'))