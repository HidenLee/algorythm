T = int(input())
for test_case in range(1,T+1):
    size, M = map(int,input().split())
    table = [list(map(int,input().split()))for _ in range(size)]
    N = size
    if N % 2:
        N = N + 1
    houselist = [(i,j) for i in range(size) for j in range(size) if table[i][j]==1]
    K = 1
    maxh = 0
    while K <= N+1:
        for y1 in range(size):
            for x1 in range(size):
                lst = [[y2,x2] for y2,x2 in houselist if abs(y1-y2)+abs(x1-x2) < K]
                if len(lst) * M >= K*K+(K-1)*(K-1) and maxh < len(lst):
                    maxh = len(lst)
        K += 1
    print(f'#{test_case} {maxh}')