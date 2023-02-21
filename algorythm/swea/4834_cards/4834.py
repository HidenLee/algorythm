T= int(input()) # 테스트케이스의 수 입력
for test_case in range(1,T+1):
    N = int(input()) # 각 케이스 카드의 수 입력
    cards = list(map(int,str(input()))) # 각 카드의 크기 모음을 리스트의 형태로 저장
    temp = cards[0]
    for card in cards:
        if cards.count(temp) < cards.count(card): # 카드의 수가 더 많으면 저장!
                temp = card
        if cards.count(temp) == cards.count(card) and temp < card: # 카드의 갯수는 같지만 value가 더 높으면 저장!
             temp = card

    print(f'#{test_case} {temp} {cards.count(temp)}')

