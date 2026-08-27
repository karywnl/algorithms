class ArrayBinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        self.tree.append(value)

    def delete(self, value):
        if len(self.tree) == 0 or value not in self.tree:
            return False

        idx = self.tree.index(value)
        self.tree[idx] = self.tree[-1]
        self.tree.pop()

        return True

    def inorder(self, idx=0):
        if idx >= len(self.tree):
            return 

        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2 

        self.inorder(left_idx)
        print(self.tree[idx], end=" ")
        self.inorder(right_idx)



binary_tree = ArrayBinaryTree()
values = [10, 20, 30, 40, 50, 60]

for x in values:
    binary_tree.insert(x)

binary_tree.delete(30)

print(binary_tree.tree)
print()


binary_tree.inorder()


