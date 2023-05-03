N = int(input())

series = 666
count = 0

while True:
    if '666' in str(series):
        count += 1
    if count == N:
        print(series)
        break
    series += 1

