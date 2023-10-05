import sys

N = int(input())
numbers = [0]*10001 # N >= 10,000

for _ in range(N):
    num = int(sys.stdin.readline())
    numbers[num] += 1

for i in range(10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)

