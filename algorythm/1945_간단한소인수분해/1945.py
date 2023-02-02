T = int(input()) # 테스트케이스
for test_case in range(T):
    num = int(input()) # 숫자 입력
    rst = [] # 결과를 저장할 리스트
    for elm in [2,3,5,7,11]: # 확인할 인수는 2,3,5,7,11 5가지
        cnt = 0 # 카운팅을 위한 변수 초기화
        while num % elm == 0: #인수로 나눠진다면~
            num /= elm # 나눈값을 다시 저장 그리고 반복!
            cnt += 1 # 반복횟수 저장
        rst.append(cnt) # 특정 요소로 더이상 나눠지지않으면 횟수 저장하고 다음 요소로 탐색
    print(f'#{test_case+1}',end=' ') # 출력양식을 맞추기위해 포맷팅 활용
    print(*rst,sep=' ')           # 리스트의 요소만 출력하기위해 asterlisk사용  
    