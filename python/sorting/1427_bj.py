numbers = list(map(str, input()))
numbers.sort(reverse=True)
for i in numbers:
    print(i, end="")
