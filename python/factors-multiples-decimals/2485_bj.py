import sys
import math

input = sys.stdin.readline

N = int(input())
trees = []
distance = []
for i in range(N):
    trees.append(int(input()))
    if i > 0:
        distance.append(trees[i] - trees[i-1])

max_distance = math.gcd(distance[0], distance[1])
for i in range(1, N-1):
    max_distance = math.gcd(max_distance, distance[i])

print((trees[-1] - trees[0]) // max_distance + 1 - N)
