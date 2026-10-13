m = 5 
table = [None] * m

def insert(value):
    for i in range(m):
        idx = (value % m + i**2) % m

        if table[idx] is None:
            table[idx] = value
            return True
        elif table[idx] == value:
            return False
    return False

def search(value):
    for i in range(m):
        idx = (value % m + i**2) % m

        if table[idx] is None:
            return False

        if table[idx] == value:
            return True
    return False