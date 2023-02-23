def sumofnode(n):
    if n > N:
        return 0
    elif tree[n] != 0:
        return tree[n]
    else:
        return sumofnode(n*2) + sumofnode(n*2+1)


T = int(input())
for test_case in range(1,T+1):
    N , M , L = map(int,input().split())
    tree = [0] * (N+1)
    for _ in range(M):
            i, j = map(int,input().split())
            tree[i] = j
    print(f'#{test_case} {sumofnode(L)}')