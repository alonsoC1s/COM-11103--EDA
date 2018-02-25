class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.h = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        else:
            return node.h

    def fe(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.right) - self.height(node.left)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        x.h = max(self.height(x.left), self.height(x.right)) + 1
        y.h = max(self.height(y.left), self.height(y.right)) + 1

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y
        x.h = max(self.height(x.left), self.height(x.right)) + 1
        y.h = max(self.height(y.left), self.height(y.right)) + 1

    def insert_fix_up(self, z):
        if z is None:
            return
        z.h = max(self.height(z.left), self.height(z.right)) + 1
        if self.fe(z) == -2:
            if self.fe(z.left) == 1:
                self.left_rotate(z.left)
            self.right_rotate(z)
        elif self.fe(z) == 2:
            if self.fe(z.right) == -1:
                self.right_rotate(z.right)
            self.left_rotate(z)
        self.insert_fix_up(z.p)

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
        self.insert_fix_up(z.p)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.__insert(key)
