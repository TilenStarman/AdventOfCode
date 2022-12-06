file = open("input.txt", "r")
lines = file.readlines()

rez = 0
stop = []

for x in lines[0]:

    stop.append(x)
    rez += 1

    if len(stop) >= 4:

        abeceda = [0] * 26

        for letter in stop:
            ind = ord(letter) - 97
            abeceda[ind] += 1

        if all(i <= 1 for i in abeceda): break
        else: stop.pop(0)
        
        
print(rez)