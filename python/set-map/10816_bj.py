import sys

input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
checks = [*map(int, input().split())]

dic = {}
for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for card in checks:
    result = dic.get(card)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
