#https://www.acmicpc.net/problem/27977

L,N,K = map(int,input().split())
arr = list(map(int,input().split()))

dist = [arr[i]-arr[i-1] for i in range(N)]


def is_success(size):
    temp = -1
    count = 0
    for i in range(N):
        if arr[i] > temp:
            count += 1
            temp = arr[i] + size - 1
            
        if count > K:
            return False
            
    return count <= K

# L//K <= size <= L
min_size = max(dist)
left, right = min_size, L

while left < right:
    mid = (left + right) // 2
    print(left,right,mid)
    if is_success(mid):
        right = mid
        if right == left:
            break
    else:
        left = mid + 1

print(right)

# 10 5 5
# 0 2 4 6 8
# 1 3 5 8 9
# 2 98 99
# 100 5 3