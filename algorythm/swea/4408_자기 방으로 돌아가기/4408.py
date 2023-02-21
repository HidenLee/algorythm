T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    cnts = [0] * (200+1)
    for _ in range(N):
        now, to = map(int, input().split())
        left = min((now-1)//2, (to-1)//2)
        right = max((now-1)//2, (to-1)//2)
        for i in range(left, right+1):
            cnts[i] += 1
    rst = max(cnts)

    print(f'#{test_case} {rst}')