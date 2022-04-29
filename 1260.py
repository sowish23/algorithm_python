from sys import stdin
from collections import deque

n, m, v = map(int,stdin.readline().split())
edge = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, stdin.readline().strip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for e in edge:
    e.sort()
    
d_check = [False for _ in range(n+1)]
def dfs(x):
    d_check[x] = True
    print(x, end = ' ')
    for y in edge[x]:
        if d_check[y] == False:
            dfs(y)
            
dfs(v)

def bfs():
    queue = deque([v])
    b_check = [False for _ in range(n + 1)]
    b_check[v] = True
    while queue: 
        for i in queue:
            print(i)
        vi = queue.popleft()
        print(vi, end = ' ')
        for i in edge[vi]:
            if not b_check[i]:
                b_check[i] = True
                queue.append(i)
print()
bfs()

