N = int(input())
cnt = 0
color = list(map(int,input().split()))
if color[0] != 0:
    cnt += 1
for _ in range(N-1):
    a, b = map(int,input().split())
    if color[a-1] != color[b-1]:
        cnt += 1
print(cnt)