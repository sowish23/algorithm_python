from sys import stdin

n = int(input())
m = int(input())

edge = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, stdin.readline().strip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)
 
for e in edge:
    e.sort()
    
d_check = [False for _ in range(n+1)]

cnt = 0
def dfs(x):
    global cnt
    d_check[x] = True
    for i in edge[x]:
        if d_check[i] == False:
            cnt += 1
            dfs(i)
    
dfs(1)
print(cnt)