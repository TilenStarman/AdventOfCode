file = open("input.txt", "r")

lines = file.readlines()
rez = 0

for x in lines:
    x = x.strip()
    first, second = x.split(",")

    first = first.split("-")
    second = second.split("-")

    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        rez += 1

    elif int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]): 
        rez += 1
    


print(rez)