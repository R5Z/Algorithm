triangle = sorted(list(map(int, input().split())))

if triangle[0] + triangle[1] > triangle[2]:
    print(sum(triangle))
else:
    print((triangle[0] + triangle[1]) * 2 - 1)
