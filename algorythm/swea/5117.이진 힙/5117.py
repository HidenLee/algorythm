T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    heap = [0] * (N+1)
    last = 0
    lst = list(map(int,input().split()))
    for num in lst:
        last += 1
        heap[last] = num
        idx = last
        while idx > 0:
            if heap[idx] < heap[idx//2]:
                heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx = idx // 2
    rst = 0
    while N > 0:
        N = N // 2
        rst += heap[N]
    print(f'#{test_case} {rst}')