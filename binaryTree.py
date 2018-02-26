class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.p = None


class BinaryTree:
    def __init__(self, *args):
        self.root = None
        if len(args) == 1:
            for x in args[0]:
                self.insert(x)

    def transplant(self, x, y):
        if x.p is None:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        if y is not None:
            y.p = x.p

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            x = self.root
            y = x.p
            while x is not None:
                y = x
                if key < x.key:
                    x = x.left
                else:
                    x = x.right
            x = Node(key)
            if key < y.key:
                y.left = x
                x.p = y
            else:
                y.right = x
                x.p = y

    def delete(self, key):
        z = self.find(key)
        if z is None:
            return
        elif z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y.left = z.left
            y.left.p = y
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)

    def __inorder__(self, x):
        if x is None:
            return []
        else:
            return self.__inorder__(x.left) + [x.key] + self.__inorder__(x.right)

    def inorder(self):
        return self.__inorder__(self.root)


tree = BinaryTree([2, 5, 8, 3, 6, 1, 7, 4])
print(tree.inorder())