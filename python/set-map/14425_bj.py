import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
count = 0

for _ in range(N):
    S = input().rstrip()
    dic[S] = 1

for i in range(M):
    check = input().rstrip()
    if check in dic:
        count += 1

print(count)
