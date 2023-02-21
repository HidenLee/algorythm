T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    rst = 0
    for i in range(n):
        for j in range(n):
            for delta in [(0,1),(0,-1),(1,0),(-1,0)]:
                newi ,newj = i + delta[0], j + delta[1]
                if 0 <= newi <= n-1 and 0 <= newj <= n-1:
                    rst += abs(array[i][j]-array[newi][newj])
    print(f'#{test_case} {rst}')                