N = int(input())
x = 0

for i in range(N):
    nums = list(map(int, str(i)))
    if N == sum(nums) + i:
        x = i
        break

print(x)
