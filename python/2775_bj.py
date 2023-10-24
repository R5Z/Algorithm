# F4 = 1 6 21 56 126 ...
# F3 = 1 5 15 35 70 ...
# F2 = 1 4 10 20 35 ...
# F1 = 1 3 6 10 15 ...
# F0 = 1 2 3 4 5 ...

# F loor, room N um

T = int(input())

for i in range(T):
    F = int(input())
    N = int(input())

    F0 = [x for x in range(1, N + 1)]

    for k in range(1, F + 1):
        for i in range(1, N):
            F0[i] += F0[i-1]
    print(F0[-1])

    
