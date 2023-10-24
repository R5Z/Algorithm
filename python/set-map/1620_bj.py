import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pokedex = {}

for i in range(1, N+1):
    pokemon = input().rstrip()
    pokedex[i] = pokemon
    pokedex[pokemon] = i

for _ in range(M):
    quest = input().rstrip()
    if quest.isdigit():
        print(pokedex[int(quest)])
    else:
        print(pokedex[quest])
    