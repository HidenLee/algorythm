'''
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.
Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.
위 문장에서 ti 를 검색하면, 답은 4이다.

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
문장의 길이는 1000자를 넘어가지 않는다.
한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.
한 문장에서는 하나의 문자열만 검색한다. 

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''
#Boyer-Moore
def BMsearch(pattern,text):
    idx = len(pattern) - 1
    cnt = 0
    while idx < len(text):
        if text[idx] in pattern:
            idx += pattern[::-1].index(text[idx])
            if text[idx-len(pattern)+1:idx+1] == pattern:
                cnt += 1
                idx += len(pattern)
            else:
                idx += 1
                    
        else:
            idx += len(pattern)
    return cnt       
    

#KMP
def KMPsearch(pattern,text):
    
    def pre_process(pattern):
        lps = [0] * len(pattern)
        #lps를 만들기 위해 패턴 인덱스
        j = 0
        # 처음부터 끝까지 순회
        for i in range(1,len(pattern)):
            #패턴 발견, 해당 인덱스의 char이 똑같다면
            if pattern[i] == pattern[j]:
                lps[i] = j + 1
                j += 1
            else:
                j = 0
                if pattern[i] == pattern[j]:
                    lps[i] = j+ 1
                    j += 1
        return lps

    next = pre_process(pattern)
    idx = 0
    j = 0
    while idx < len(pattern):
        while j > 0 and text[idx] != pattern[j]:
            j = next[j-1]
        if text[idx] == pattern[j]:
            if j == len(pattern)-1:
                print(idx-len(pattern)+1)
                j = next[j]    






for _ in range(1):
	# n= int(input())
    n =1 
    str1='ti'
    lst1='Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition'
    print(f'#{n} {BMsearch(str1,lst1)}')
    KMPsearch()