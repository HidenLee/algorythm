T = int(input())
for test_case in range(1,T+1):
    nums = list(map(int,input().split()))
    N = len(nums)
    true_or_false = 0
    for i in range(1<<N):
        rst = 0
        for j in range(N):
            if i & (1<<j):
                rst += nums[j]
        if rst == 0 and i != 0: # 공집합도 부분집합인데 sum했을때 0나와서 코드를 부수니까 여기서 배제
            true_or_false = 1
            break    
    print(f'#{test_case} {true_or_false}')    