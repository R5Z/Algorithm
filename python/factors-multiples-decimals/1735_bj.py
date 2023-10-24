import math

a, b = map(int, input().split())
c, d = map(int, input().split())

# ex) (2*5+2*7) / 7*5 = 31 / 35
result1, result2 = a*d+b*c, b*d
gcd = math.gcd(result1, result2)
if gcd != 1:
    result1 //= gcd
    result2 //= gcd

print(result1, result2)
