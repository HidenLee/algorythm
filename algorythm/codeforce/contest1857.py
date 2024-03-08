# https://codeforces.com/contest/1857/problem/B

def problemB():
    for i in range(int(input())):
        ipt = input()
        ans = ipt
        k = -1
        flag = False
        for i in range(len(ipt)):
            target = int(ipt[i])
            if target >= 5:
                k = i
                for j in range(i-1,-1,-1):
                    if j < 0: 
                        break
                    elif int(ipt[j]) != 4: 
                        k = j
                        break
                else: 
                    k = 0
                break
        if k > 0:
            Head = int(ipt[:k])
            Body = int(ipt[k])
    
            if Body == 9:
                Head += 1
                Body = 0
            else:
                Body += 1
            ans = str(Head) + str(Body) + "0"*(len(ipt)-k-1)

        elif k == 0:
            Body = int(ipt[k])

            if Body >= 4:
                Body = 10
            else:
                Body += 1
            ans = str(Body) + "0"*(len(ipt)-k-1)


        else:
            if int(ipt[0]) < 5:
                ans = ipt
            else:
                ans = 10**(len(ipt))
        print(int(ans))


#  https://codeforces.com/contest/1857/problem/C
# import math
for i in range(int(input())):
    N = int(input())
    ans = []
    dic = {}
    for j in list(map(int,input().split())):
        if j in dic: dic[j] += 1
        else: dic[j] = 1
    # srzlst = sorted([(x,y) for x,y in dic.items()],key=lambda X : dic[X[0]], reverse=True)
    ans.extend(dic.keys())
    while len(ans) < N:
        ans.append(max(ans))

    # print("ans: ",ans)
    print(ans)

    # print(srzlst)