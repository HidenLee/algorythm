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
alphadict = {}
numlist = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
hashset =set([])
for num in numlist:
    hashset.update(list(num))
hashlist = sorted(list(hashset)) #sorted

hashstring = 'EFGHINORSTUVWXZ' # sorted
for idx, alpha in enumerate(hashstring):
    alphadict[alpha] = idx

def sol(string1):
    cnt = [0 for _ in range(len(hashstring))]
    for a in string1:
        cnt[alphadict[a]] += 1
    
    while sum(cnt):
        for alpha in numlist:
            
    ans = ''
    
    return



for tc in range(1,int(input())+1):
    print(f'Case #{tc}: {sol(input())}')
