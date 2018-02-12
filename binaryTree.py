class Node:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None
	

class Tree:
	def __init__(self):
		self.root = None
	
	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			self._insert(self.root, val)
	
	def _insert(self, actual, val):
		if val < actual.val:
			if actual.left == None:
				actual.left = Node(val)
			else:
				self._insert(actual.left, val)
		else:
			if actual.right == None:
				actual.right = Node(val)
			else:
				self._insert(actual.right, val)
	

def inorder(u):
	if u != None:
		inorder(u.left)
		print u.val
		inorder(u.right)
		

tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(4)
tree.insert(-2)
tree.insert(0)
inorder(tree.root)