# https://www.acmicpc.net/problem/5719 거의 최단 경로

from collections import deque

Big = 10e9

# def findRoute(S, D, graph):
#     N = len(graph)
#     deq = deque([(S,[S])])
#     node = [Big for _ in range (N)]
#     node[S] = 0
#     minRoute = []
#     minLangth = Big
#     while deq:
#         now, route = deq.pop()
#         for nxt in range(N):
#             if graph[now][nxt] != -1 and node[now] + graph[now][nxt] <= node[nxt]:
#                 node[nxt] = node[now] + graph[now][nxt]
#                 deq.appendleft((nxt,route+[nxt]))
#                 if nxt == D:
#                     if node[D] == minLangth:
#                         minRoute.append(route+[nxt])
#                     elif node[D] < minLangth:
#                         minLangth = node[D]
#                         minRoute = [route+[nxt]]
#     return minRoute, minLangth

def Dijkstra(graph, s):
    costlist = [Big for _ in range(N)]
    route = [[]for _ in range(N)]
    queue = deque([(s,0)])
    costlist[s] = 0
    while queue:
        onode, ocost = queue.popleft()
        if ocost > costlist[ocost]:
            continue
        for nnode, ncost in enumerate(graph[onode]):
            if ncost != -1:
                if costlist[nnode] > costlist[onode] + ncost:
                    costlist[nnode] = costlist[onode] + ncost
                    route[nnode] = [onode]
                    queue.append((nnode,ncost))
                elif costlist[nnode] == costlist[onode] + ncost:
                    route[nnode].append(onode)
    print("costlist: ", costlist)
    return route, costlist
    
def deleteBFS(d, route, graph): # delete from destination - backward tracking
    visit = [False for _ in range(N)]
    visit[d] = True
    deq = deque([d])
    while deq:
        onode = deq.popleft()
        for nnode in route[onode]:
            if not visit[nnode]:
                deq.append(nnode)
                visit[nnode] = True
            graph[nnode][onode] = -1
    return graph

while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    S, D = map(int, input().split())
    graph = [[-1 for _ in range(N)] for _ in range (N)]
    
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U][V] = P
    
    # minRoute, minLangth = findRoute(S, D, graph)

    # for mr in minRoute:
    #     for idx in range(1,len(mr)):
    #         graph[mr[idx-1]][mr[idx]] = -1
    
    # minRoute, minLangth = findRoute(S, D, graph)

    minRoute, _ = Dijkstra(graph,S)
    graph = deleteBFS(D,minRoute,graph)
    _, ans = Dijkstra(graph, S)
    print(ans[D] if ans[D] != Big else -1)

    # if minRoute:
    #     print(minLangth)
    #     # print(minRoute)
    # else:
    #     print(-1)

def solution():
    import sys
    from collections import deque

    def dijkstra(graph, costlist, s):
        minload = [[]for x in range(n)]
        queue = deque([(s, 0)])
        costlist[s] = 0
        while queue:
            # print("queue", queue)
            node, cost = queue.popleft()
            if cost > costlist[node]:
                continue
            for nnode, ncost in graph[node]:
                if ncost != -1:
                    if costlist[nnode] > costlist[node] + ncost:
                        costlist[nnode] = costlist[node]+ncost
                        minload[nnode].clear()
                        minload[nnode].append(node)
                        queue.append((nnode, ncost))
                        # print("update", node, nnode, minload)
                    elif costlist[nnode] == costlist[node] + ncost:
                        minload[nnode].append(node)
                        # print("add", node, nnode, minload)
        # print(minload)
        return minload

    def bfs(d, minload, visit, graph):
        queue = deque([d])
        visit[d] = True
        while queue:
            node = queue.popleft()
            for nnode in minload[node]: # node: 도착, nnode: 출발
                if visit[nnode]==False:
                    queue.append(nnode)
                    visit[nnode]=True
                for index in range(len(graph[nnode])):
                    if graph[nnode][index][0] == node:
                        graph[nnode][index][1] = -1
        return graph

    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            exit()
        graph = [[]for x in range(n)]
        s, d = map(int, sys.stdin.readline().split())
        for i in range(m):
            u, v, p = map(int, sys.stdin.readline().split())
            graph[u].append([v, p])
        costlist = [1e10 for x in range(n)]

        # 최단 경로 구하기
        minload = dijkstra(graph, costlist, s)
        # 최단 경로 제거
        visit = [False for x in range(n)]
        bfs(d, minload, visit, graph)
        # 거의 최단 경로 구하기
        costlist = [1e10 for x in range(n)]
        dijkstra(graph, costlist, s)
        if costlist[d] == 1e10:
            print(-1)
        else:
            print(costlist[d])