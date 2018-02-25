from Node import *


class AVLTree:
    def __init__(self, *args):
        self.root = None
        if len(args) == 1:
            for x in args[0]:
                self.insert(x)

    def height(self, node):
        if node is None:
            return 0
        else:
            return node.h

    def update_height(self, node):
        node.h = max(self.height(node.left), self.height(node.right)) + 1

    def fe(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.right) - self.height(node.left)

    def find(self, key):
        it = self.root
        while it is not None and it.key != key:
            if key < it.key:
                it = it.left
            else:
                it = it.right
        return it

    def transplant(self, x, y):
        if x.p is None:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        if y is not None:
            y.p = x.p

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        self.transplant(x, y)
        y.left = x
        x.p = y
        self.update_height(x)
        self.update_height(y)
        
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        self.transplant(x, y)
        y.right = x
        x.p = y
        self.update_height(x)
        self.update_height(y)

    def fix_up(self, z):
        while z is not None:
            self.update_height(z)
            if self.fe(z) == -2:
                if self.fe(z.left) == 1:
                    self.left_rotate(z.left)
                self.right_rotate(z)
            elif self.fe(z) == 2:
                if self.fe(z.right) == -1:
                    self.right_rotate(z.right)
                self.left_rotate(z)
            z = z.p

    def _insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < y.key:
                x = y.left
            else:
                x = y.right
        z.p = y
        if key < y.key:
            y.left = z
        else:
            y.right = z
        self.fix_up(z.p)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key)

    def minimum(self, node):
        x = node
        while x.left is not None:
            x = x.left
        return x

    def delete(self, key):
        z = self.find(key)
        x = None
        if z.left is None:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is None:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
                x = y.p
            else:
                x = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
        self.fix_up(x)

    def _inorder(self, nodo):
        if nodo is not None:
            return self._inorder(nodo.left) + [nodo.key] + self._inorder(nodo.right)
        else:
            return []

    def inorder(self):
        return self._inorder(self.root)