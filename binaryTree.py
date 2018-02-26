class Node:
	def __init__(self, key):
		self.key = key
		self.right = None
		self.left = None
		self.p = None
	

class Tree:
	def __init__(self):
		self.root = None
	
	def find(self, key):
		it = self.root
		while it.key != key:
			if key < it.key:
				it = it.left
			else:
				it = it.right
		return it
	
	def insert(self, key):
		if self.root is None:
			self.root = Node(key)
		else:
			self._insert(self.root, key)
	
	def _insert(self, actual, key):
		if key < actual.key:
			if actual.left is None:
				actual.left = Node(key)
				actual.left.p = actual
			else:
				self._insert(actual.left, key)
		else:
			if actual.right is None:
				actual.right = Node(key)
				actual.right.p = actual
			else:
				self._insert(actual.right, key)
	
	def transplant(self, x, y):
		if x.p is None:
			self.root = y
		elif x.p.left == x:
			x.p.left = y
		else:
			x.p.right = y
		if y is not None:
			y.p = x.p
		
	def minimum(self, u):
		it = u
		while it.left != None:
			it = it.left
		return it
	
	def delete(self, key):
		it = self.find(key)
		if it.left is None:
			self.transplant(it, it.right)
		elif it.right is None:
			self.transplant(it, it.left)
		else:
			y = self.minimum(it.right)
			if y.p != it:
				self.transplant(y, y.right)
				y.right = it.right
				y.right.p = y
			self.transplant(it, y)
			y.left = it.left
			y.left.p = y

def height(u):
	if u is None:
		return 0
	else:
		return 1 + max(height(u.left), height(u.right))

def inorder(u):
	if u != None:
		inorder(u.left)
		print u.key
		inorder(u.right)
		

tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(4)
tree.insert(-2)
tree.insert(0)
tree.delete(3)
inorder(tree.root)
