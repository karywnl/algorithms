m = 10

table = [[] for _ in range(m)]

def insert(key):
    h_x = key % m
    if key not in table[h_x]:
        table[h_x].append(key)
        return True
    return False

values = [22, 12, 32, 32]

for value in values:
    insert(value)

print(table)