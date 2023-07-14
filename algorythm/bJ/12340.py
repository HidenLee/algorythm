# https://www.acmicpc.net/problem/12340
# Fair and Square (Large1) 


# def ispalindrome(x):
#     reversed_num = 0
#     num = x
#     while num > 0:
#         reversed_num = reversed_num * 10 + num % 10
#         num //= 10
#     return x == reversed_num

# def issquare(x):
#     sqrt = int(x**0.5)
#     return sqrt * sqrt == x

# def issuperpalindrome(x):
#     if not ispalindrome(x):
#         return False
#     sqrt = int(x**0.5)
#     return issquare(x) and ispalindrome(sqrt)


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



T = int(input())
for test_case in range(1,T+1):
    L, R = map(int,input().split())
    ans = 0
    for iterator in range(L,R+1):
        if issuperpalindrome(iterator):
            ans += 1
    print(f'Case #{test_case}: {ans}')
    