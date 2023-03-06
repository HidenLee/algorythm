T = int(input())
for test_case in range(1,T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int,input().split()))
    # bbang = K * (t // M)
    customer.sort(reverse=True)
    t = 0
    ans = 'Possible'
    BBang = 0
    while customer:
        t += customer.pop()
        BBang = K * (t//M) - (N - len(customer))
        if BBang < 0:
            ans = 'Impossible'
            break
    print(f'#{test_case} {ans}')