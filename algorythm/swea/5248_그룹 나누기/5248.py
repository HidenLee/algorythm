def mergeset(idx1,idx2):
    if arr[idx2]:
        arr[idx1] |= arr[idx2]
        arr[idx2].clear()
        return
    else:
        for i in range(1,N+1):
            if idx2 in arr[i]:
                mergeset(idx1,i)
                return
        else:
            mergeset(idx2,idx1)

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [set([_]) for _ in range(N+1)]
    lst = list(map(int,input().split()))
    for i in range(M):
        fr , to = lst[2*i] ,lst[2*i+1]
        for j in range(1,N+1):
            if fr in arr[j] and to != j:
                mergeset(j,to)
            elif to in arr[j] and fr != j:
                mergeset(j,fr)
    print(f'#{test_case} {len([i for i in arr if i])-1}')