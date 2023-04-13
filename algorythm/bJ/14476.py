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
# print(leftgcd)
# print(rightgcd)

for i in range(len(lst)):
    if i == 0:
        temp = rightgcd[1]
    elif i == len(lst)-1:
        temp = leftgcd[-2]
    else:
        temp = gcd(leftgcd[i-1],rightgcd[-i-2])
    if lst[i] % temp:
        print(temp,lst[i])
        break
else:
    print(-1)
