def cal(n,tree):
    n = int(n)
    if tree[n][0] == '+':
        return cal(tree[n][1],tree) + cal(tree[n][2],tree)
    elif tree[n][0] == '-':
        return cal(tree[n][1],tree) - cal(tree[n][2],tree)
    elif tree[n][0] == '*':
        return cal(tree[n][1],tree) * cal(tree[n][2],tree)
    elif tree[n][0] == '/':
        return cal(tree[n][1],tree) / cal(tree[n][2],tree)
    else:
        return int(tree[n][0])
         


T = 10
for test_case in range(1,T+1):
    N = int(input())
    lst = [0] *  (N + 1)
    for _ in range(N):
       n, *m =  input().split()
       lst[int(n)] = m
    print(f'#{test_case} {cal(1,lst)}')