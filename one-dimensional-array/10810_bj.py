N, M = map(int, input().split())
basket = [0] * N

for x in range(M):
    i, j, k = map(int, input().split())
    for index in range(i, j+1):
        basket[index-1] = k
for i in range(N):
    print(basket[i], end=" ")

# 1 2 1 1 0 % 요렇게 출력되는데 정답이라고 뜨네? 왜?