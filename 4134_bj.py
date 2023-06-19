import sys

input = sys.stdin.readline

N = int(input())

def check(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

for _ in range(N):
    j = int(input())
    while True:
        if j == 0 or j == 1:
            print(2)
            break
        if check(j):
            print(j)
            break
        else:
            j += 1
        
