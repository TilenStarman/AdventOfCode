file = open("input.txt", "r")
lines = file.readlines()



path =  []
dicl = {}

for x in lines: 
    x = x.strip()

    if x[0:4] == '$ cd':
        dest = x[5:]

        if dest == '..':
            path.pop()

        else:
            path.append(dest)

    elif x[0:4] == '$ ls':
        continue

    else:
        try:
            value,_ = x.split()
            value = int(value)

            for i in range(1, len(path) + 1):
                if '/'.join(path[:i]) not in dicl:
                    dicl['/'.join(path[:i])] = value
                else:
                    dicl['/'.join(path[:i])] += value
            
        except:
            pass

print(dicl)


rez = 0
m = 1E9

freeSpace = dicl['/'] - 40000000
print(freeSpace)

for x in dicl.values():
    if (x <= 100000):
        rez += x

    if x >= freeSpace:
        m = min(m, x)

print(rez) #part1
print(m)   #part2