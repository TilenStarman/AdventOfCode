file = open("input.txt", "r")
lines = file.readlines()

value = 0
vsota = 0

for i in range(0, len(lines), 3):
    x1 = set(lines[i].strip())
    x2 = set(lines[i + 1].strip())
    x3 = set(lines[i + 2].strip())

    common = x1 & x2 & x3
    a = list(common)
    v = ord(a[0]) #idk ord je bil retard

    if (a[0].isupper()):
        value = v - 38
    else:
        value = v - 96
    
    vsota += value

print(vsota)