# N, M = map(int,input().split())
# dic = {X:set() for X in range(1,N+1)}
# for _ in range(M):
#     a, b = map(int,input().split())
#     dic[a].add(b)
#     dic[b].add(a)


# # 정리된 그래프를 bfs 탐색 (모든 노드에 대해 수행하니까 global visit 필요) 제자리 순환 홀수 depth면 망함
# gvisit = set()
# from collections import deque 

# def bfs(start):
#     deq = deque([(start,0,0)])
#     while deq:
#         now, past, depth = deq.pop()
#         if now == start and past!= 0:
#             if depth % 2:
#                 return False
#             else:
#                 continue
#         for nxt in dic[now]:
#             if nxt != past:
#                 deq.appendleft((nxt,now,depth+1))
#     return True

# for i in range(1,N+1):
#     if i in gvisit:
#         continue
#     if bfs(i):
#         gvisit.add(i)
#     else:
#         print(0)
#         break
# else:
#     print(1)


from collections import deque

N, M = map(int, input().split())
dic = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

gvisit = [0] * (N + 1)

def bfs(start):
    queue = deque([(start, 0)])
    gvisit[start] = 1
    
    while queue:
        now, depth = queue.popleft()
        
        for nxt in dic[now]:
            if gvisit[nxt] == 0:
                gvisit[nxt] = gvisit[now] * -1  # 서로 다른 집합으로 나누기 위해 반대 부호 사용
                queue.append((nxt, depth + 1))
            elif gvisit[nxt] == gvisit[now]:
                return False  # 이분 그래프가 아님
    
    return True

for i in range(1, N + 1):
    if gvisit[i] == 0:  # 방문하지 않은 노드에서 BFS 시작
        if not bfs(i):
            print(0)
            break
else:
    print(1)