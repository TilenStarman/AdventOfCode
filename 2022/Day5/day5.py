file = open("input.txt", "r")
lines = file.readlines()

ind = 0

for x in lines:
    x = x.strip()

    if x == "": 
        break
    ind += 1

#-----------------------------------
start = lines[:ind-1]
#na ind-1 so "tla"

stTabel = len(lines[ind - 1].split())
startPos = [""] * stTabel

for x in start:

    i = 0

    # [start:stop:step]
    # vsak cetrti char je crka
    for y in x[1::4]:
        
        if y != " ": 
            startPos[i] += y

        i += 1
                
#-----------------------------------
moves = lines[ind+1:]
endPos = startPos[:]

for x in moves:
    _, n, _, src, _, dest = x.split()
    n = int(n)
    src = int(src) - 1
    dest = int(dest) - 1

    print(endPos)
    print('move ', n, ' from ', src, ' to ', dest)

    for i in range(0, n):
        endPos[dest] = endPos[src][i] + endPos[dest]

    endPos[src] = endPos[src][n:]

rez = ''

for x in endPos:
    rez += x[0]

print(rez)
