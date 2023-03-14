N = int(input())
possible = [(r,c) for r in range(N) for c, v in enumerate(list(map(int, input().split())))  if v]
print(possible)
length = 0
n = list()
for r1, c1 in possible:
    tmp = -1
    for r2, c2 in possible:
        if r1+c1 == r2+c2 or r1-c1 == r2-c2:
            tmp += 1
    n.append((tmp, r1, c1))
    length += 1


n.sort()
i = 0
answer = 0
while i < length:
    if n[i][0] > -1:
        j = i + 1
        while j < length:
            if n[i][1] + n[i][2] == n[j][1] + n[j][2] or n[i][1] - n[i][2] == n[j][1] - n[j][2] :
                n[j] = (-1, -1, -1)
            j += 1
        answer += 1
    i += 1

print(answer)