m = 5
table = [None] * m

def insert(key):
    for i in range(m):
        idx = (key % m + i) % m
        if table[idx] is None:
            table[idx] = key
            return True
        elif table[idx] == key:
            return False
    return False

def search(key):
    for i in range(m):
        idx = (key % m + i) % m
        if table[idx] is None:
            return False
        if table[idx] == key:
            return True
    return False

values = [12, 22, 32, 42, 22]

for value in values:
    insert(value)

print(table)
print(search(42))