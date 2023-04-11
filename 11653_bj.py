N = int(input())
i = 2 # 2부터 나누기 시작

while (N > 1):
    if N%i == 0:
        N = N/i
        print(i)
    else:
        i += 1
