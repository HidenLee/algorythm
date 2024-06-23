# https://www.acmicpc.net/problem/1325
N, M = map(int,input().split())
trust = [set() for _ in range(N+1)]
ans = []
maxSize = 0
for _ in range(M):
    A, B = map(int,input().split())
    trust[B].add(A)

# fail - time out
def sol_dfs(N, trust, maxSize):
    for idx in range(1,N+1):
        stack = [idx]
        visit = [False]*(N+1)
        cnt = 0
        while stack:
            old = stack.pop()
            if visit[old]:
                continue
            visit[old] = True
            cnt += 1
            for new in trust[old]:
                if not visit[new]:
                    stack.append(new)
        if (maxSize <cnt):
            maxSize = cnt
            ans = [idx]
        elif (maxSize == cnt):
            ans.append(idx)
    return ans


# pass
from collections import deque
def sol_bfs(N, trust, maxSize):
    for idx in range(1, N+1):
        dq = deque([idx])
        visit = [False] *(N+1)
        visit[idx] = True
        cnt = 0
        while dq:
            old = dq.popleft()
            cnt += 1
            for nxt in trust[old]:
                if visit[nxt]:
                    continue
                else:
                    dq.append(nxt)
                    visit[nxt] = True
        if (maxSize <cnt):
            maxSize = cnt
            ans = [idx]
        elif (maxSize == cnt):
            ans.append(idx)
    return ans



ans1 = sol_dfs(N, trust, maxSize)
ans2 = sol_bfs(N, trust, maxSize)

print(*ans1)
print(*ans2)


