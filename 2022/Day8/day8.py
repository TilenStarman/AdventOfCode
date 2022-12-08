file = open("input.txt", "r")
lines = file.readlines()

grid = []

for x in lines: 
    x = x.strip()
    grid.append([int(digit) for digit in x ])
    

test = [[0] * len(grid) for _ in range(len(grid))]



lrmax = -1
tdmax = -1

# left to right, top to bottom
for i in range(0, len(grid)):
    for j in range(0, len(grid)):

        if grid[i][j] > lrmax:
            lrmax = grid[i][j]
            test[i][j] = 1
        
        if grid[j][i] > tdmax:
            tdmax = grid[j][i]
            test[j][i] = 1
    
    lrmax = -1
    tdmax = -1

# right to left, bottom to top
for i in range(len(grid) - 1, -1, -1):
    for j in range(len(grid) - 1, -1, -1):

        if grid[i][j] > lrmax:
            lrmax = grid[i][j]
            test[i][j] = 1
        
        if grid[j][i] > tdmax:
            tdmax = grid[j][i]
            test[j][i] = 1
    
    lrmax = -1
    tdmax = -1



rez = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):

        if test[i][j] == 1:
            rez += 1

#print(grid)
#print(test)
print(rez)