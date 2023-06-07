S = input()
strings = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        strings.add(S[i:j+1])

print(len(strings))

