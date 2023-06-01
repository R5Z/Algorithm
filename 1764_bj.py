import sys

input = sys.stdin.readline

N, M = map(int, input().split())

x = [input().strip() for i in range(N)] # 문자열 및 공백 제거
y = [input().strip() for i in range(M)]

duplicate = list(set(x) & set(y))

print(len(duplicate))
for someone in sorted(duplicate):
    print(someone)


# N, M = map(int, input().split())

# x = set()
# for _ in range(N):
#     x.add(input().rstrip())

# y = set()
# for _ in range(M):
#     y.add(input().rstrip())

# duplicate = sorted(list(x & y))

# print(len(duplicate))
# for someone in duplicate:
#     print(someone)
