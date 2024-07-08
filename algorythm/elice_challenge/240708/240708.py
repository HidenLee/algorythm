num = [int(x) for x in input()]
N= len(num)

flag = False

for ridx in range(N-1,0,-1):
    for lidx in range(ridx-1,-1,-1):
        if num[lidx] < num[ridx]:
            num[lidx], num[ridx] = num[ridx], num[lidx]
            num = num[:lidx+1] + sorted(num[lidx+1:])
            flag = True
            break
    if flag:
        break

ans = sum([num[x]*10**(N-1-x) for x in range(N)])
print(ans)