from collections import deque

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    lst = list(map(int, input().split()))
    for i in range(lst[1]): # 0이면 바로 스킵
        graph[lst[0]].append(lst[i+2])
        indegree[lst[i+2]] += 1


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for g in graph[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    if any(indegree):
        print(-1)
        exit()

    # 위상 정렬 수행한 결과 출력
    for res in result:
        print(res, end=' ')

topology_sort()

# 7 8
# 1 2 2 5
# 2 2 3 6
# 3 1 4
# 4 1 7
# 5 1 6
# 6 1 4
# 7 1 6
# 2 0
