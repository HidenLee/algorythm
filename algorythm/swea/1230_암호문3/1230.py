def recotype(n):
    if n in ["I","A","D"]:
        return str(n)
    else:
        return int(n)

for tc in range(1,11):
    N = int(input())
    lst = list(map(int, input().split()))
    M = int(input())
    Mlst = list(map(recotype,input().split()))
    for idx in range(len(Mlst)):
        if Mlst[idx] == "I": # I X Y S
            X = int(Mlst[idx + 1])
            Y = int(Mlst[idx + 2])
            for j in range(Y):
                lst.insert(X+j,int(Mlst[idx+3+j]))
            # X, S = int(Mlst[idx+1]), Mlst[idx + 3 : idx + 3 + Y]
            # lst[X:X] = S #use list slicing
        elif Mlst[idx] == "D": # D X Y
            X, Y = int(Mlst[idx+1]), int(Mlst[idx + 2])
            for j in range(Y):
                del lst[X]
        elif Mlst[idx] == "A": # A Y S
            Y = int(Mlst[idx+1]) 
            for j in range(Y):
                lst.append(Mlst[idx+j+2])
    ans = lst[:10]
    print(f'#{tc} {" ".join(map(str, ans))}')