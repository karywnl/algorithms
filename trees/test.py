tree = [None] * 8

def insert(value):
    idx = 0
    while idx < len(tree):
        if tree[idx] is None:
            tree[idx] = value
            return 
        elif value < tree[idx]:
            idx = 2 * idx + 1
        elif value > tree[idx]:
            idx = 2 * idx + 2
        else:
            print("dupicate value")
            return 
    print("not enough space to insert")

def search(value):
    idx = 0
    while idx < len(tree) and tree[idx] is not None:
        if tree[idx] == value:
            return idx
        elif value < tree[idx]:
            idx = 2 * idx + 1
        elif value > tree[idx]:
            idx = 2 * idx + 2
    return -1 

def inorder(idx=0):
    if idx >= len(tree) or tree[idx] is None:
        return

    inorder(2 * idx + 1)
    print(tree[idx], end=" ")
    inorder(2 * idx + 2)
    