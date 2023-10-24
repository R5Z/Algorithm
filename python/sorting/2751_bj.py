import sys

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

for i in sorted(numbers):
    print(i)
    