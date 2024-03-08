import random



def check(num):
    strike = 0
    ball = 0
    for idx, n in enumerate(num):
        if n in ANS:
            if ANS[idx] == n:
                strike += 1
            else:
                ball += 1
    return strike, ball








ANS = "".join(map(str,random.sample(list(range(0,10)),4))) #1234?
print(ANS)


strike, ball  = check

