file = open("input.txt", "r")

lines = file.readlines()
value = 0
vsota = 0

for x in lines:
    x = x.strip()
    backpack = list(x)
    first = backpack[:len(backpack)//2]
    second = backpack[len(backpack)//2:]

    f = set(first)
    s = set(second)

    common = f & s
    a = list(common)
    v = ord(a[0]) #idk ord je bil retard

    if (a[0].isupper()):
        value = v - 38
    else:
        value = v - 96
    
    vsota += value

print(vsota)