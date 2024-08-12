from collections import deque
N, M = map(int,input().split())
if N >= M :
    print(N-M)
else:
    queue = deque([N])
    # stack = [(N,0)]
    # visit = set([])
    table = [1000000]*100001
    table[N] = 0
    ans = 0
    while(queue):
        now = queue.popleft()
        if now == M:
            break
        for nxt in [now*2,now-1,now+1]:
            if 0<=nxt<=100000 and table[nxt] > table[now] + 1:
                table[nxt] = table[now] + 1
                queue.append(nxt)

    # while (stack):
    #     print(stack)
    #     now, depth = stack.pop()
    #     if now == M:
    #         ans = depth
    #         break
    #     for nxt in [now*2,now-1,now+1]:
    #         if nxt <= M+1 and nxt not in visit:
    #             stack.append((nxt,depth+1))
    #             visit.add(nxt)
    print(table[M])
        