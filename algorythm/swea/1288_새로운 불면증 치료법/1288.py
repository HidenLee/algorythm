for tc in range(1,int(input())+1):
    lst = [0]*10
    N = int(input())
    k = 1
    while sum(lst) != 10:
        now = N*k
        for n in str(now):
            if not lst[int(n)]:
                lst[int(n)] = 1
        k = k + 1
    print(f'#{tc} {now}')