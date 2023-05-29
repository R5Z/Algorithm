N = int(input())
dic = {}

for _ in range(N):
    name, status = input().split()
    dic[name] = status
    if status == "leave":
        del dic[name]
    
stay = sorted(dic.items(), reverse=True)
dic = dict(stay)

for key in dic.keys():
    print(key)

