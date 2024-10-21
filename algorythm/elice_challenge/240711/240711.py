N = int(input())
route = {x:[] for x in range(N+1)}
visit = [False for _ in range(N+1)]
iswin = [0 for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int,input().split())
    route[u].append(v)
    route[v].append(u)

INF = 10e12

def find_min_diff(node):
    visit[node] = True
    diff = INF
    for child in route[node]:
        if not visit[child]:
            diff = min(diff, find_min_diff(child))
    if diff == INF:
        diff = 0
    if diff <= node:
        iswin[node] = 1
    return node - diff


find_min_diff(1)
for i in range(1,N+1):
    print(iswin[i])