

for test_case in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [1]*N
    ans = 999
    for i in range(1<<N):
        temp = 0
        for j in range(N):
            if temp < B and i & (1<<j):
                temp += arr[j]
            
        if ans > temp - B >= 0:
            ans = temp - B
    print(f'#{test_case} {ans}')
