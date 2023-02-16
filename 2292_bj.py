# 1, 1+6, 1+6+12, 1+6+12+18, ... 

N = int(input())

cnt = 1
honeycomb = 1

while N > honeycomb:
    honeycomb += 6 * cnt # multiple of 6
    cnt += 1

print(cnt)