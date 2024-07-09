n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    i , j , k = map(int, input().split())
    narr = arr[i-1:j]
    print(sorted(narr)[k-1])