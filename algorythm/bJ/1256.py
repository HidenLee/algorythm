faclist = [1]
for i in range(1,41):
    faclist.append(faclist[-1]*i)
comblist = [faclist[2*t]//(faclist[t])**2 for t in range(21)]
print(comblist)




def func(N,M,K):
    head = ''
    tail = ''
    for idx, comb in enumerate(comblist):
        if K < comb:
            T = (idx+1) -1
            break
    else:
        return -1

    if T <= N and T <= M:
        head = 'a'*(N-T)
        tail = 'z'*(M-T)
    elif 2*T <= N+M:
        if N > M:
            T = M
            head = 'a'*(N-T)
        else:
            T = N
            tail = 'z'*(M-T)
    else:
        return -1

    rst = head + func(T,T,) + tail





N,M,K = map(int,input().split())
rst = ''