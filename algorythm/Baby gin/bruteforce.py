def perm(i,k):
    if i == k:
        perms.append(p[:])
    else:
        for j in range(k):
            if not used[j]:
                p[i] = N[j]
                used[j] = True
                perm(i+1,k)
                used[j] = False


def perm2(arr,a):
    rst = []
    if a > len(arr):
        return rst
    if a == 1:
        for i in arr:
            rst.append(arr[i])
    elif a > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm2(ans,a-1):
                rst.append(z)




T = int(input())
for test_case in range(T):
    N = list(map(int,str(input())))
    perms = []
    p = [0]*6
    used = [0]*6
    perm(0,6)
    for each in perms:
        if each[0]+each[2] == (each[1]*2) and each[3]+each[5] == (each[4]*2): 
            if each[1]-each[0] in [-1,0,1] and each[4]-each[3] in [-1,0,1]:
                print("True")
                break
    else:
        print(len(perms))
        print("False")