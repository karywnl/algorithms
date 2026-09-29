
tree = [None] * 4

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
            print("duplicate value")
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

def delete(value):
    pass

def inorder(idx=0):
    if idx >= len(tree) or tree[idx] is None:
        return 

    inorder(2 * idx + 1)
    print(tree[idx], end=" ")
    inorder(2 * idx + 2)


values = [20, 10, 30, 5]
for value in values:
    insert(value)

inorder()