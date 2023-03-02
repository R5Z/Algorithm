N, M = map(int, input().split())
basket = []

for x in range(N):
    basket.append(x + 1)

for x in range(M):
    i, j = map(int, input().split())
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]

for x in range(N):
    print(basket[x], end=" ")
