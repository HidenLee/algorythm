from collections import deque
N, M = map(int,input().split())
route = {}
for _ in range(N+M):
    fr, to = map(int,input().split())
    route[fr] = to
dist = [100000]*101
dist[1] = 0
deq = deque([1])
while deq:
    now = deq.popleft()
    if now in route:
        deq.append(route[now])
        dist[route[now]] = min(dist[route[now]],dist[now])
        continue
    for nxt in [x for x in range(now+1,now+7) if x <101]:
        if dist[nxt] > dist[now] + 1:
            dist[nxt] = dist[now] + 1
            deq.append(nxt) 
print(dist[100])