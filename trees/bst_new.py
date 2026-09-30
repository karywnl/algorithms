tree = []


# ---------- INSERTION ----------
# Smaller -> Left
# Larger  -> Right

def insert(value):

    if len(tree) == 0:
        tree.append(value)
        return

    i = 0

    while True:

        if value < tree[i]:
            i = 2 * i + 1

        elif value > tree[i]:
            i = 2 * i + 2

        else:
            print("Duplicate value")
            return

        # Create space if required
        while i >= len(tree):
            tree.append(None)

        if tree[i] is None:
            tree[i] = value
            return


# ---------- SEARCH ----------

def search(value):

    i = 0

    while i < len(tree) and tree[i] is not None:

        if tree[i] == value:
            return i

        elif value < tree[i]:
            i = 2 * i + 1

        else:
            i = 2 * i + 2

    return -1
    



    


