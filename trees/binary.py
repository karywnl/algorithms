def insert(tree, value):
    # looking for gaps to insert
    for idx, node in enumerate(tree):
        if node is None:
            tree[idx] = value
            return idx

    # no gaps found so insert in the last
    tree.append(value)
    return len(tree) - 1

def delete(tree, value):

    # selecting the last node for none
    last_idx = -1
    while tree[last_idx] is None:
        last_idx -= 1
        tree.pop()

    # replacing the value with right most value (last inserted value)
    # deleted the last value
    for i in range(len(tree)):
        if tree[i] == value:
            tree[i] = tree[last_idx]
            tree.pop()
            return True
    return False


tree = [10, 12, 15, None, 8]
delete(tree, 12)
print(tree)
delete(tree, 15)
print(tree)