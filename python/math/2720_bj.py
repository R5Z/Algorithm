T = int(input())
changes = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    for i in changes:
        print(C//i, end=' ')
        C = C%i
