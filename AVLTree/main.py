from AVLTree import *

values = [7, 4, 3, 8, 2, 6, 1, 5]
tree = AVLTree(values)

print(tree.inorder())
for x in values:
    tree.delete(x)
    print(tree.inorder())
