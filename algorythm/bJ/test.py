def perm(i,k):
    if i ==k:
        # print(p)
        if not p in perms:
            perms.append(p)
    else:
        for j in range(k):
            if not used[j]:
                p[i] = N[j]
                used[j] = True
                perm(i+1,k)
                used[j] = False
                



T = int(input())
for test_case in range(T):
    N = list(map(int,str(input())))
    perms = []
    p = [0 for _ in range(len(N))]
    used = [0 for _ in range(len(N))]
    perm(0,len(N))
    # for each in perms:
    #     if each[0]+each[2] == each[1]*2 and each[3]+each[5] == each[4]*2 and -1 <= each[1]-each[0] <= 1 and -1 <= each[4]-each[3] <= 1:
    #         print("True")
    #         break
    # else:
    #     print("False")
    print(perms)