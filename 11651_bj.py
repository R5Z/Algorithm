N = int(input())
array = []

for i in range(N):
    x, y = map(int, input().split())
    array.append([y, x])
sorted_array = sorted(array)
for y, x in sorted_array:
    print(x, y)
