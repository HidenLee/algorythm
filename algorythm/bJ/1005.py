def totalbuildT(b):
    if not builds[b]: 
        return times[b-1]
    else:
        return times[b-1] + max([totalbuildT(a) for a in builds[b]])

def totalbuildT2(b,builds):
    visited = []
    stack = builds[b][:]
    while stack:
        targetbd = stack.pop()
        if not targetbd in visited:
            visited.append(targetbd)
            stack.extend(builds[targetbd])
            



T = int(input())
for test_case in range(T):
    N, K = map(int,input().split())
    builds = [[] for _ in range(N+1)]
    times  = list(map(int,input().split()))
    for _ in range(K):
        a, b = map(int,input().split())
        builds[b].append(a)
    W = int(input())
    rst = totalbuildT(W)
    rst = totalbuildT2(W,builds)
    print(rst)
