K = int(input())
baskets = list(map(int,input().split()))
# arr_windx = sorted([(x,arr[x]) for x in range(4)],key=lambda X: X[1])
# while True:
    
# print(arr_windx)
def move_eggs_to_one_basket(K, baskets):
    # print("Initial State:", baskets)
    # print(*baskets)
    
    steps = 0
    total_eggs = sum(baskets)
    
    while baskets.count(0) < 3 and steps < K:
        # 계란이 하나 이상 있는 바구니 인덱스와 계란 수를 추출
        non_empty_baskets = [(i, baskets[i]) for i in range(4) if baskets[i] > 0]
        
        # 계란이 적은 순서로 정렬
        non_empty_baskets.sort(key=lambda x: x[1])
        
        # 계란이 하나 이상 들어있는 두 바구니 선택
        a = non_empty_baskets[0][0]  # 가장 적은 계란을 가진 바구니
        b = non_empty_baskets[1][0]  # 두 번째로 적은 계란을 가진 바구니
        
        # 나머지 바구니를 찾기
        for i in range(4):
            if i != a and i != b:
                c = i
                break
        
        # 두 계란 이동
        baskets[a] -= 1
        baskets[b] -= 1
        baskets[c] += 2
        steps += 1
        
        # print(f"Step {steps}: {baskets}")
        print(*baskets)
    
    # 최종 상태 출력
    final_state = [0, 0, 0, 0]
    max_index = baskets.index(max(baskets))
    final_state[max_index] = total_eggs
    # print(f"Final State: {final_state}")
    # print(*final_state)

# Input 처리
# K = int(input("Enter the number of operations allowed: "))  # 최대 작업 횟수
# baskets = list(map(int, input("Enter the number of eggs in each basket: ").split()))

# 계란 이동
move_eggs_to_one_basket(K, baskets)