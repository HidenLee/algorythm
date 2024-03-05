""" 
ZERO
ONE
TWO
THREE
FOUR
FIVE
SIX
SEVEN
EIGHT
NINE
ONETWHRFUIVSXGZ
"""
numlist = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

#THREE의 E가 두개라서 예외처리 버그
def sol1(string1): 
    alphadict = {}
    hashset =set([])
    for num in numlist:
        hashset.update(list(num))
    hashlist = sorted(list(hashset)) #sorted
    hashstring = 'EFGHINORSTUVWXZ' # sorted
    for idx, alpha in enumerate(hashlist):
        alphadict[alpha] = idx

    cnt = [0 for _ in range(len(hashstring))]
    for a in string1:
        cnt[alphadict[a]] += 1
    ans = ''
    while sum(cnt):
        print(cnt)
        for num in numlist:
            temp = []
            for alpha in num:
                if cnt[alphadict[alpha]]:
                    temp.append(alphadict[alpha])
                else:
                    break
            else:
                ans += num
                for i in temp:
                    cnt[i] -= 1
    return ans

#bruteforce
def sol2(string1): 
    numlist = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
    numlist2 = numlist + numlist
    i = 0
    while True: 
        ans = ''
        string2 = list(string1)
        for num in numlist2[i:i+10]:
            while True:
                temp = [0 for _ in range(len(num))]
                for alpha in string2:
                    for idx in range(len(num)):
                        if alpha == num[idx] and temp[idx] == 0:
                            temp[idx] += 1
                            break
                    if len(num) == sum(temp):
                        ans += str(numlist.index(num))
                        for n in num:
                            string2[string2.index(n)] = '0'
                        break
                else:
                    break
        if any( s != "0" for s in string2):
            i += 1
        else:
            return ans
            
#bruteforce in short
def sol3(string1): 
    ans = ''
    string2 = list(string1)
    # while 'Z' in string2:
    for num in ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']:
        while all(string2.count(ch) >= num.count(ch) for ch in num):
            ans += str(numlist.index(num))
            for ch in num:
                string2.remove(ch)
    return ''.join(sorted(ans))  # Sort the digits in ascending order


##Idea - 02468 => ZWUXG 고유문자
def sol4(string1): 
    ans = [0 for _ in range(10)]
    keyword = 'ZOWRUFXSGI'
    kdict = {keyword[X]:X for X in range(len(keyword))}
    for s in string1:
        if s in keyword:
            ans[kdict[s]] += 1
    ans[1] = ans[1] - ans[0] - ans[2] - ans[4]
    ans[3] = ans[3] - ans[0] - ans[4]
    ans[5] = ans[5] - ans[4]
    ans[7] = ans[7] - ans[6]
    ans[9] = ans[9] - ans[5] - ans[6] - ans[8]
    buffer = ''
    for idx, i in enumerate(ans):
        buffer += str(idx)*i
    return buffer

for tc in range(1,int(input())+1):
    print(f'Case #{tc}: {sol4(input())}')



#반례 ONEINTW => 29
# print(sol2('ONEINTW'))

##Idea - 02468 => ZWUXG 고유문자
