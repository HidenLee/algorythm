# from collections import deque
# T = int(input())
# for test_case in range(1,T+1):
#     word = deque(input())
#     while True:
#         try: 
#             if word.popleft() == word.pop():
#                 pass
#             else:
#                 print(f'#{test_case} 0')
#                 break
#         except:
#                 print(f'#{test_case} 1')
#                 break

T = int(input())
for test_case in range(1,T+1):
    word = input()
    if word == word[::-1]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
        

# T = int(input())
# for test_case in range(1,T+1):
#     word = list(input())
#     idx = 0
#     for idx in range(int(len(word)/2)):
#         if word[idx] != word.pop():
#             print(f'#{test_case} 0')
#             break
#     else:
#         print(f'#{test_case} 1')
   
