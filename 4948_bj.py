from math import sqrt

m = 123456 # 1 <= n <= 123,456

num_list = [True for _ in range(2*m+1)]
num_list[0], num_list[1] = False, False # 0, 1 제외

for i in range(2, int(sqrt(2*m)+1)):
    if num_list[i]:
        j = 2
        while i * j <= 2 * m:
            num_list[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break

    count = 0

    for i in range(n+1, 2*n+1):
        if num_list[i]:
            count += 1
        
    print(count)