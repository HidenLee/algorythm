

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [set([_]) for _ in range(N+1)]
    lst = list(map(int,input().split()))
    for i in range(M):
        fr , to = lst[2*i] ,lst[2*i+1]
        for j in range(1,N+1):
            if fr in arr[j] and to != j:
                arr[j] |= arr[to]
                arr[to].clear()
                
            elif to in arr[j] and fr != j:
                arr[j] |= arr[fr]
                arr[fr].clear()
        print(fr,to,arr)
    print(f'#{test_case} {len([i for i in arr if i])-1}')