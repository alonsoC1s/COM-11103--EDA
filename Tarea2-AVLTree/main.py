from AVLTree import *

values = [100, 300, 400, 350, 375, 50, 200, 360]
tree = AVLTree(values)
print(tree)
for x in [300, 360, 350]:
    print('Elimina ' + str(x))
    tree.delete(x)
    print(tree)
