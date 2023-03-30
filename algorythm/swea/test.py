def func1(nowchance, visited, depth):
    global maxchance
    if depth == N and maxchance < nowchance:
        maxchance = nowchance
        return nowchance
    elif nowchance <= maxchance:
        return 0
    for idx, nxt in enumerate(lst[depth]):
        nxt = nxt / 100
        if not visited[idx] and nxt:
            visited[idx] = True    
            nowchance *= nxt
            nowchance = max(func1(nowchance,visited,depth+1), nowchance)
            nowchance /= nxt
            visited[idx] = False
    return nowchance



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    maxchance = float(0)
    for i in range(len(lst[0])):
        visited = [False]*N
        visited[i] = True
        temp = func1(lst[0][i]/100, visited, 1)
    print("#{} {:.6f}".format(test_case, maxchance*100))
