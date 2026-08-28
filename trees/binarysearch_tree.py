class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedBST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)

        elif value > root.value:
            root.right = self.insert(root.right, value)

        return root

    def delete(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left = self.delete(root.left, value)

        elif value > root.value:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            successor = root.right

            while successor.left is not None:
                successor = successor.left

            root.value = successor.value
            root.right = self.delete(root.right, successor.value)

        return root
        

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is None:
            return 

        self._inorder(node.left)
        print(node.value, end=" ")
        self._inorder(node.right)


        
        
    
            

class ArrayBinarySearchTree:
    def __init__(self, size=15):
        self.tree = [None] * size

    def insert(self, value):
        idx = 0

        while True:
            if idx >= len(self.tree):
                self.tree.extend(
                    [None] * (idx - len(self.tree) + 1)
                )

            if self.tree[idx] is None:
                self.tree[idx] = value
                return True

            if value < self.tree[idx]:
                idx = 2 * idx + 1
            elif value > self.tree[idx]:
                idx = 2 * idx + 2
            else:
                return False

    def delete(self, value):
        if value not in self.tree:
            return False

        idx = self.tree.index(value)
        remaining = [
            item
            for position, item in enumerate(self.tree)
            if item is not None and position != idx
        ]

        self.tree = [None] * len(self.tree)

        for item in remaining:
            self.insert(item)

        return True


bst = LinkedBST()

values = [20, 10, 30, 5, 50]
for x in values:
    bst.root = bst.insert(bst.root, x)

bst.inorder()
