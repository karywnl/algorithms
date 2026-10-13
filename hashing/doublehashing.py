m = 5 
table = [None] * m

def insert(value):
    for i in range(m):
        h1 = value % m
        h2 = 1 + (value % (m - 1))
        idx = (h1 + i * h2) % m

        if table[idx] is None:
            table[idx] = value
            return True
        elif table[idx] == value:
            return False
    return False

def search(value):
    for i in range(m):
        h1 = value % m
        h2 = 1 + (value % (m - 1))
        idx = (h1 + i * h2) % m

        if table[idx] is None:
            return False

        if table[idx] == value:
            return True
    return False

def rehash(new_m):
    global table, m
    old_table = table
    old_m = m
    m = new_m
    table = [None] * m

    for i in range(old_m):
        if old_table[i] is not None:
            insert(old_table[i])