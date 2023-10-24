# F loor, R oom number 
# F = guest // H

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    F = N % H
    R = N // H + 1
    if F == 0: # H == W 일 때
        R -= 1
        F = H
    
    print(F * 100 + R)