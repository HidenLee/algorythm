T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = []
    print(f'#{test_case}')
    for rows in range(N):
        if len(a) < 2:
            a.append(1)    
        else:
            b=[1]
            for idx in range(len(a)-1):
                b.append(a[idx]+a[idx+1])
            b.append(1)
            a = b    
        print(*a)