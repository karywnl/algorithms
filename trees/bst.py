
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

def find_min(idx):
    left_idx = 2 * idx + 1

    while left_idx < len(tree) and tree[left_idx] is not None:
        idx = left_idx
        left_idx = 2 * left_idx + 1
        
    return idx

def move_subtree(source, destination):
    moves = []

    def collect(src, dst):
        if src >= len(tree) or tree[src] is None:
            return
        moves.append((src, dst, tree[src]))
        collect(2 * src + 1, 2 * dst + 1)
        collect(2 * src + 2, 2 * dst + 2)

    collect(source, destination)

    # Clear old positions before writing new positions.
    for src, dst, value in moves:
        tree[src] = None

    for src, dst, value in moves:
        tree[dst] = value

        
def delete(value):
    idx = search(value)

    if idx == -1:
        return

    left_idx = 2 * idx + 1
    right_idx = 2 * idx + 2

    has_left = left_idx < len(tree) and tree[left_idx] is not None
    has_right = right_idx < len(tree) and tree[right_idx] is not None

    # Case 1: No children
    if not has_left and not has_right:
        tree[idx] = None

    # Case 2: Only a left child
    elif has_left and not has_right:
        move_subtree(left_idx, idx)

    # Case 2: Only a right child
    elif has_right and not has_left:
        move_subtree(right_idx, idx)

    # Case 3: Two children
    else:
        successor_idx = find_min(right_idx)

        tree[idx] = tree[successor_idx]
        tree[successor_idx] = None

        # The successor may have a right child.
        successor_right = 2 * successor_idx + 2
        move_subtree(successor_right, successor_idx)


def inorder(idx=0):
    if idx >= len(tree) or tree[idx] is None:
        return 

    inorder(2 * idx + 1)
    print(tree[idx], end=" ")
    inorder(2 * idx + 2)


values = [20, 10, 30, 5, 2]
for value in values:
    insert(value)

delete(5)
print(tree)