with open('input.txt', 'r') as file: data = file.read().replace('\n', ' ')
dic = {}
x = 1
cycle = 0
value = 0
words = data.split()
for word in words:
    cycle += 1
    x += value
    dic[cycle] = x
    if word == 'noop' or word == 'addx': value = 0
    else: value = int(word)
print(dic[20] * 20 + dic[60] * 60 + dic[100] * 100 + dic[140] * 140 + dic[180] * 180 + dic[220] * 220)
screen = [['..'] * 40 for _ in range(6)]
for i in range(0, 6):
    for j in range(0, 40):
        c = i * 40 + j + 1
        if abs(dic[c] - j) <= 1: screen[i][j] = '##'
for row in screen: print(''.join(row))