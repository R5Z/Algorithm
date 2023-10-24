M = int(input())
N = int(input())
primeNum = []

for i in range(M, N+1):
    if i == 1:
        pass
    elif i == 2:
        primeNum.append(i)
    else:
        for j in range(2, i):
            if i%j == 0:
                break
            elif j == i-1:
                primeNum.append(i)

if len(primeNum) == 0:
    print(-1)
else:
    print(sum(primeNum))
    print(min(primeNum))
    