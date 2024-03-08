# https://www.acmicpc.net/problem/12340
# Fair and Square (Large1)
# continued to No. 12341  


# def ispalindrome(x):
#     reversed_num = 0
#     num = x
#     while num > 0:
#         reversed_num = reversed_num * 10 + num % 10
#         num //= 10
#     return x == reversed_num

import itertools

def generate_featable_palindrome(L):
    #generate all featable square roots of length 2*L+1 or 2*L
    yield 1
    yield 2
    yield 3

    #The case that start/end with 1 : 2n=> 1111001111,200002 / 2n+1 => 110020011,11110101111, 2001002
    #The case that start/end with 2 : 2n=> 200002 / 2n+1 => 2001002  
    for h in range(L):
        for n_ones in range(1,5):
            for ones in itertools.combinations(range(h),n_ones-1):
                a = ['0']*h
                for i in ones:
                    a[i] = '1'
                s = '1' + ''.join(a)
                rs = s[::-1]
                yield int(s+rs)
                yield int(s+'0'+rs)
                yield int(s+'1'+rs)

                if n_ones <= 2:
                    yield int(s+'2'+rs)

        s = '2' + '0'*h
        rs = s[::-1]
        yield int(s+rs)
        yield int(s+'0'+rs)
        yield int(s+'1'+rs)


def ispalindrome(x):
    s = str(x)
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    else:
        return True


def issquare(x):
    return True if int(x**0.5)**2 == x else False


def issuperpalindrome(x): 
    return True if ispalindrome(x) and issquare(x) and ispalindrome(int(x**0.5)) else False

def rangePreprocessing(m,n):
    sm = str(m)

    q, r = divmod(len(sm), 2)
    # Note here that r = len(sm)%2.  If r is 0, we duplicate the middle digit and
    # generate palindromes like 1221.  If r is 1, we don't duplicate the middle
    # digit, instead generating palindromes like 12321.

    # lh is the "left half" of the palindrome we are generating
    lh = int(sm[:(q + r)])

    while True:
        slh = str(lh)

        # Check for rollover (99 becoming 100, for example)
        if len(slh) != q + r:
            if r == 0:
                # We go from generating numbers like 9999 to 10001, i.e. with an odd
                # length
                r = 1
            else:
                # We go from generating numbers like 99999 to 100001, i.e. with an even
                # length
                q, r = q + 1, 0
                # We don't want lh to increase in length yet
                lh = lh//10
                slh = slh[:-1]

        # wh is the "whole" palindrome, made by mirroring lh
        if r == 0:
            # slh[::-1] is the same tricky slice syntax for reversing a string
            wh = int(slh + slh[::-1])
        else:
            # More tricky slice syntax: slh[-2::-1] reverses slh, except for the last
            # character
            wh = int(slh + slh[-2::-1])

        if wh >= n:
            # We hit the upper bound
            return
        elif wh >= m:
            yield wh

        # Increment the left half and go again
        lh += 1



all_superpalindromes = list(map(lambda x:x*x,generate_featable_palindrome(25)))

T = int(input())
for test_case in range(1,T+1):
    L, R = map(int,input().split())
    # sqL, sqR = int((L-1)**0.5)+1, int(R**0.5)
    ans = 0
    # for iterator in rangePreprocessing(sqL,sqR+1):
    #     if ispalindrome(iterator**2):
    #         ans += 1
    for iterator in all_superpalindromes:
        if L <= iterator <= R:
            ans+=1
    print(f'Case #{test_case}: {ans}')
    
