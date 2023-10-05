import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

sorted_numbers = sorted(list(set(numbers)))
dic = {sorted_numbers[i]:i for i in range(len(sorted_numbers))}

for i in numbers:
    print(dic[i], end=" ")

