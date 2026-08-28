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

    def _inorder(self, root):
        if root is None:
            return None

        self._inorder(root.left)
        print(root.value, end=" ")
        self._inorder(root.right)


bst = LinkedBST()
values = [20, 10, 30, 5, 50]
for x in values:
    bst.root = bst.insert(bst.root, x)

bst.inorder()
