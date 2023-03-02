T = int(input())
for test_case in range(1,T+1):
    ans = ['' for _ in range(15)]
    code = []
    for _ in range(5):
        code.append(input())
    
    for idx in range(15):
        for _ in range(5):
            if len(code[_]) > idx:
                ans[idx%15] = ans[idx%15] + code[_][idx]
    print(f"#{test_case} {''.join(ans)}")
