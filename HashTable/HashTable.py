from HashNode import *


class HashTable:
    def __init__(self):
        self.arr = [None]
        self.cnt = 0

    def resize(self):
        newArr = [None] * (len(self.arr)*2 + 1)

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
            if list is not None:
                it = list
                res += str(it.dato)
                it = it.next
                while it is not None:
                    res += ', ' + str(it.dato)
                    it = it.next
            res += '}\n'
        return res
