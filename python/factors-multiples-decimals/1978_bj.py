N = int(input())
numbers = list(map(int, input().split()))
count = 0

for x in numbers:
    for i in range(2, x+1):
        if x%i == 0:
            if x == i:
                count += 1
            
            break

print(count)