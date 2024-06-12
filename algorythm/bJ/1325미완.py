# https://www.acmicpc.net/problem/1325


N, M = map(int,input().split())
trust = [[] for _ in range(N+1)]
ans = []
maxSize = 0
for _ in range(M):
    A, B = map(int,input().split())
    trust[B].append(A)
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

print(*ans)

