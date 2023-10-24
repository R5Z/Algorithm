a1, a0 = map(int, input().split())
c = int(input())
n = int(input())
x = 1 if a1*n+a0 <= c*n and c >= a1 else 0
print(x)


# same code

# if score >= 60:
#     message = "success"
# else:
#     message = "failure"

# =

# message = "success" if score >= 60 else "failure"