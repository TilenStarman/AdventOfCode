file = open("input.txt", "r")
lines = file.readlines()

global vH
global vT


def toKey(x, y):
    return str(x) + ' ' + str(y)

def getX(key):
    x,_ = key.split()
    return int(x)

def getY(key):
    _, y = key.split()
    return int(y)

def areAdjacent(a, b):

    if abs(getX(a) - getX(b)) <= 1 and abs(getY(a) - getY(b)) <= 1:
        return True
    else:
        return False

def moveRight(head, tail, steps):

    global vH
    global vT

    tmp = head

    x = getX(head)
    y = getY(head)
    for i in range(x + 1, x + steps + 1):
        tmp = head
        

        if not toKey(i, y) in grid:
            grid[toKey(i, y)] = vH
        elif toKey(i, y) in grid and not grid[toKey(i, y)] == vT:
            grid[toKey(i, y)] = vH
        

        head = toKey(i, y)

        if not areAdjacent(head, tail):
            tail = tmp
            grid[tail] = vT

    
    return head, tail

def moveLeft(head, tail, steps):

    global vH
    global vT

    tmp = head

    x = getX(head)
    y = getY(head)
    for i in range(x - 1, x - steps - 1, -1):
        tmp = head

        if not toKey(i, y) in grid:
            grid[toKey(i, y)] = vH
        elif toKey(i, y) in grid and not grid[toKey(i, y)] == vT:
            grid[toKey(i, y)] = vH


        head = toKey(i, y)

        if not areAdjacent(head, tail):
            tail = tmp
            grid[tail] = vT
            


    return head, tail

def moveUp(head, tail, steps):

    global vH
    global vT

    tmp = head

    x = getX(head)
    y = getY(head)
    for i in range(y + 1, y + steps + 1):
        tmp = head


        if not toKey(x, i) in grid:
            grid[toKey(x, i)] = vH
        elif toKey(x, i) in grid and not grid[toKey(x, i)] == vT:
            grid[toKey(x, i)] = vH

        head = toKey(x, i)

        if not areAdjacent(head, tail):
            tail = tmp
            grid[tail] = vT

    return head, tail

def moveDown(head, tail, steps):

    global vH
    global vT

    tmp = head

    x = getX(head)
    y = getY(head)
    for i in range(y - 1, y - steps - 1, -1):
        tmp = head

        if not toKey(x, i) in grid:
            grid[toKey(x, i)] = vH
        elif toKey(x, i) in grid and not grid[toKey(x, i)] == vT:
            grid[toKey(x, i)] = vH

        head = toKey(x, i)

        if not areAdjacent(head, tail):
            tail = tmp
            grid[tail] = vT

    return head, tail


grid = {}

vH = 0
vT = 1

head = '0 0'
tail = '0 0'

grid[head] = 1
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    direction, steps = lines[i].split()
    steps = int(steps)

    if direction == 'R':
        head, tail = moveRight(head, tail, steps)
    if direction == 'L':
        head, tail = moveLeft(head, tail, steps)
    if direction == 'U':
        head, tail = moveUp(head, tail, steps)
    if direction == 'D':
        head, tail = moveDown(head, tail, steps)


rez = 0
for x in grid.values():
    if x == 1:
        rez += 1

print(head)
print(tail)

print(rez)