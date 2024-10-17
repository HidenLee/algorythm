N, M = map(int,input().split())
# arr = [int(input()) for _ in range(M)]



import heapq

arr = []
for _ in range(M):
    ipt = int(input())
    heapq.heappush(arr,ipt*-1)
for _ in range(N-M):
    temp = heapq.heappop(arr)*-1
    if temp % 2:
        heapq.heappush(arr,-1*(temp//2))
        heapq.heappush(arr,-1*(temp//2+1))
    else:
        heapq.heappush(arr,-1*(temp//2))
        heapq.heappush(arr,-1*(temp//2))
print(heapq.heappop(arr)*-1)