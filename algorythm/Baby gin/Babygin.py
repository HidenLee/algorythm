import sys
sys.stdin = open('input.txt','r')

T = int(input()) # 테스트케이스의 수 입력
for test_case in range(1,T+1):
    nums = list(map(int,str(input()))) # 각 숫자들을 찢어서 리스트로 저장
    babygin = 0
    for elm in nums[:]:
        if nums.count(elm) == 3 : 
            nums.remove(elm)
            nums.remove(elm)
            nums.remove(elm)
        elif nums.count(elm) == 6:
            nums.clear()
    if nums != []:
        for elm in nums[:]:
            if elm in nums and elm+1 in nums and elm+2 in nums:
                nums.remove(elm)
                nums.remove(elm+1)
                nums.remove(elm+2)
    if nums == []:
        babygin = 1        
    print(f'#{test_case} {babygin}')

