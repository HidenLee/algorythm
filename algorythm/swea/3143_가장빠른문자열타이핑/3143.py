T = int(input())
for test_case in range(1,T+1):
    word1 , word2 = input().split()
    cnt = 0
    idx = 0
    while idx < len(word1)-len(word2)+1:
        if word1[idx:idx+len(word2)] == word2:
            cnt +=1
            idx += len(word2)
        else:
            cnt += 1
            idx += 1
    if idx < len(word1):
        cnt += len(word1) - idx        
    print(f'#{test_case} {cnt}')