from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# INSERTION
def insert(root, data):
    if root is None:
        return Node(data)

    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.left is None:
            current.left = Node(data)
            return root
        else:
            queue.append(current.left)

        if current.right is None:
            current.right = Node(data)
            return root
        else:
            queue.append(current.right)


# DELETION
def delete(root, data):
    if root is None:
        return None

    # If root itself is the only node
    if root.left is None and root.right is None:
        if root.data == data:
            return None
        return root

    queue = deque([root])
    target = None
    last = None

    # Find target and deepest node
    while queue:
        current = queue.popleft()

        if current.data == data:
            target = current

        last = current

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    if target is None:
        print("Value not found.")
        return root

    # Replace target with deepest node
    target.data = last.data

    # Delete deepest node
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.left == last:
            current.left = None
            return root

        if current.right == last:
            current.right = None
            return root

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return root


# INORDER TRAVERSAL
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# MAIN
root = None

n = int(input("Enter number of nodes to insert: "))

print("Enter the values:")
for i in range(n):
    value = int(input())
    root = insert(root, value)

print("\nBinary Tree after insertion:")
inorder(root)

value = int(input("\n\nEnter value to delete: "))

root = delete(root, value)

print("\nBinary Tree after deletion:")
inorder(root)