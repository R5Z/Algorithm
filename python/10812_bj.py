N, M = map(int, input().split())
basket = [i+1 for i in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    basket[i-1:j] = basket[k-1:j] + basket[i-1:k-1]
print(*basket) 
