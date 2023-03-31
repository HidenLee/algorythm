def func1(nowcost, visited, depth):
    global ans
    if depth == N and ans > nowcost:
        ans = nowcost
        return nowcost
    elif nowcost >= ans:
        return 9999
    for idx, nxt in enumerate(factories[depth]):
        if not visited[idx]:
            visited[idx] = True
            nowcost += nxt    
            nowcost = min(func1(nowcost,visited,depth+1), nowcost)
            nowcost -= nxt    
            visited[idx] = False
    return nowcost



for _ in range(1,int(input())+1):
    N = int(input())
    factories = [list(map(int,input().split())) for _ in range(N)]
    ans = 9999
    for i in range(len(factories[0])):
        visited = [False]*N
        visited[i] = True
        temp = func1(factories[0][i], visited, 1)
    print(f'#{_} {ans}')

