def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


N = int(input())
lst = list(map(int, input().split()))

leftgcd = [lst[0]]
rightgcd = [lst[-1]]
for i in range(1,len(lst)):
    leftgcd.append(gcd(leftgcd[i-1],lst[i]))
    rightgcd.append(gcd(rightgcd[i-1],lst[-i-1]))

maxgcd = 0
targetidx = 0
for i in range(len(lst)):
    if i == 0:
        temp = rightgcd[1]
    elif i == len(lst)-1:
        temp = leftgcd[-2]
    else:
        temp = gcd(leftgcd[i-1],rightgcd[-i-2])
    if lst[i] % temp and maxgcd < temp:
        maxgcd = temp
        targetidx = i
else:
    if maxgcd:
        print(maxgcd,lst[targetidx])
    else:
        print(-1)