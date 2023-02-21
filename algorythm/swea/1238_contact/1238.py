T = 10
M = 100
for test_case in range(1,T+1):
    size, S = map(int,input().split())
    nodelist = [[] for _ in range(M+1)]
    lst = list(map(int,input().split()))
    for i in range(size//2):
        if not lst[2*i+1] in nodelist[lst[2*i]]:
            nodelist[lst[2*i]].append(lst[2*i+1])
    distance = [9999]*(M+1)
    visited = [False]*(M+1) 
    queue = [S]
    distance[S] = 0
    while queue:
        now = queue.pop(0)
        visited[now] = True
        side = [distance[X] for X in range(M+1) if now in nodelist[X]]
        side.append(distance[now])
        distance[now] = min(side) + 1
        for next in nodelist[now]:
            if not visited[next]:
                queue.append(next)
    
    final = [X for X in range(M+1) if visited[X] and distance[X]<999]
    final = sorted(final,key=lambda X: (distance[X],X))
    rst = final[-1]
    print(f'#{test_case} {rst}')