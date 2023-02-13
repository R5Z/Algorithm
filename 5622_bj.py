# input() <- str으로 처리. str(input()) <- XXX!!

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alb = input()

time = 0
for i in dial:
    for j in i:
        for x in alb:
            if j == x:
                time += dial.index(i) +3

print(time)