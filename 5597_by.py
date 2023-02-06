num = [ i for i in range(1, 31)]

for _ in range(28):
    submit = int(input())
    num.remove(submit)

print(min(num))
print(max(num))

