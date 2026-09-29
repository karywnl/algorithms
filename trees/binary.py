tree = []

def insert(value):
    tree.append(value)

def search(value):
    for i in range(len(tree)):
        if tree[i] == value:
            return i

    return -1

def delete(value):
    idx = search(value)

    if idx == -1:
        print("Value not found")
        return 

    tree[idx] = tree[-1]
    tree.pop()

def inorder(idx=0):
    if idx >= len(tree):
        return 

    inorder(2 * idx + 1)
    print(tree[idx], end=" ")
    inorder(2 * idx + 2)

def postorder(idx=0):
    if idx >= len(tree):
        return 

    postorder(2 * idx + 1)
    postorder(2 * idx + 2)
    print(tree[idx], end=" ")

def preorder(idx=0):
    if idx >= len(tree):
        return 

    print(tree[idx], end=" ")
    preorder(2 * idx + 1)
    preorder(2 * idx + 2)

vals = [10, 20, 30, 40, 50]

for x in vals:
    insert(x)

# delete(20)
# print(tree)
preorder()
print()
inorder()
print()
postorder()




