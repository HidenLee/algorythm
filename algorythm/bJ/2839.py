N = int(input())

arr = [1e9]*(N+1)
if N >= 3:
    arr[3] = 1
if N >= 5:
    arr[5] = 1
for i in range(6,N+1):
    arr[i] = min(arr[i-3],arr[i-5]) + 1
if arr[N] > 1e8:
    print(-1)
else:
    print(arr[N])


