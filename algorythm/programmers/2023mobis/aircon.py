# https://school.programmers.co.kr/learn/courses/30/lessons/214289?language=python3
'''
문제 설명
현대모비스에서 개발한 실내공조 제어 시스템은 차내에 승객이 탑승 중일 때 항상 쾌적한 실내온도(t1 ~ t21)를 유지할 수 있도록 합니다. 현재(0분) 실내온도는 실외온도와 같습니다.

실내공조 제어 시스템은 실내온도를 조절하기 위해 에어컨의 전원을 켜 희망온도를 설정합니다. 희망온도는 에어컨의 전원이 켜져 있는 동안 원하는 값으로 변경할 수 있습니다. 실내온도와 희망온도가 다르다면 1분 뒤 실내온도가 희망온도와 같아지는 방향으로 1도 상승 또는 하강합니다. 실내온도가 희망온도와 같다면 에어컨이 켜져 있는 동안은 실내온도가 변하지 않습니다.

에어컨의 전원을 끄면 실내온도가 실외온도와 같아지는 방향으로 매 분 1도 상승 또는 하강합니다. 실내온도와 실외온도가 같다면 실내온도는 변하지 않습니다.

에어컨의 소비전력은 현재 실내온도에 따라 달라집니다. 에어컨의 희망온도와 실내온도가 다르다면 매 분 전력을 a만큼 소비하고, 희망온도와 실내온도가 같다면 매 분 전력을 b만큼 소비합니다. 에어컨이 꺼져 있다면 전력을 소비하지 않으며, 에어컨을 켜고 끄는데 필요한 시간과 전력은 0이라고 가정합니다.

실내공조 제어 시스템은 차내에 승객이 탑승 중일 때 실내온도를 t1 ~ t2도 사이로 유지하면서, 에어컨의 소비전력을 최소화합니다.

다음은 실외온도가 28도, t1= 18, t2 = 26, a = 10 b = 8인 예시입니다.

시간(분)	승객 탑승
0	x
1	x
2	o
3	o
4	o
5	o
6	o
승객이 탑승 중인 2 ~ 6분의 실내온도를 18 ~ 26도 사이로 유지해야 합니다.
다음은 2 ~ 6분의 실내온도를 쾌적한 온도로 유지하는 방법 중 하나입니다.

시간(분)	승객 탑승	실내온도	희망온도
0	x	28	26
1	x	27	26
2	o	26	26
3	o	26	26
4	o	26	26
5	o	26	26
6	o	26	off
0분의 실내온도는 항상 실외온도와 같습니다.
6분에 에어컨의 전원을 껐습니다.
0 ~ 5분에 에어컨의 희망온도를 26도로 설정했습니다. 0 ~ 1분에 희망온도와 실내온도가 다르므로 전력을 매 분 10씩, 2 ~ 5분에 희망온도와 실내온도가 같으므로 전력을 매 분 8씩 소비했습니다. 이때 총 소비전력은 52(= 2 × 10 + 4 × 8)입니다.

다음은 2 ~ 6분의 실내온도를 쾌적한 온도로 유지하는 또 다른 방법입니다.

시간(분)	승객 탑승	실내온도	희망온도
0	x	28	24
1	x	27	24
2	o	26	24
3	o	25	24
4	o	24	off
5	o	25	off
6	o	26	off
0 ~ 3분에 에어컨의 희망온도를 24도로 설정해 전력을 매 분 10씩 소비했습니다. 이때 총 소비전력은 40(= 4 × 10)이며, 이보다 소비전력이 적어지는 방법은 없습니다.

실외온도를 나타내는 정수 temperature, 쾌적한 실내온도의 범위를 나타내는 정수 t1, t2, 에어컨의 소비전력을 나타내는 정수 a, b와 승객이 탑승 중인 시간을 나타내는 1차원 정수 배열 onboard가 매개변수로 주어집니다. 승객이 탑승 중인 시간에 쾌적한 실내온도를 유지하기 위한 최소 소비전력을 return 하도록 solution 함수를 완성해 주세요.

제한사항
-10 ≤ temperature ≤ 40
-10 ≤ t1 < t2 ≤ 40
temperature는 t1 ~ t2 범위 밖의 값입니다.
1 ≤ a, b ≤ 100
a는 에어컨의 희망온도와 실내온도가 다를 때의 1분당 소비전력을 나타냅니다.
b는 에어컨의 희망온도와 실내온도가 같을 때의 1분당 소비전력을 나타냅니다.
2 ≤ onboard의 길이 ≤ 1,000
onboard[i]는 0 혹은 1이며, onboard[i]가 1이라면 i분에 승객이 탑승 중이라는 것을 의미합니다.
onboard[0] = 0
onboard에 1이 최소 한 번 이상 등장합니다.
승객이 탑승 중인 시간에 쾌적한 실내온도를 유지하는 것이 불가능한 경우는 주어지지 않습니다.
입출력 예
temperature	t1	t2	a	b	onboard	result
28	18	26	10	8	[0, 0, 1, 1, 1, 1, 1]	40
-10	-5	5	5	1	[0, 0, 0, 0, 0, 1, 0]	25
11	8	10	10	1	[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]	20
11	8	10	10	100	[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]	60
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

시간(분)	승객 탑승	실내온도	희망온도
0	x	-10	40
1	x	-9	40
2	x	-8	40
3	x	-7	40
4	x	-6	40
5	o	-5	off
6	x	-6	off
0 ~ 4분에 에어컨의 희망온도를 40도로 설정하고, 5 ~ 6분에 에어컨의 전원을 끕니다. 이때 총 소비전력은 25(= 5 × 5)며, 이보다 소비전력이 적어지는 방법은 없습니다. 따라서 25를 return 해야 합니다.

입출력 예 #3

아래 표와 같이 에어컨을 조작하면 소비전력이 최소가 됩니다.

시간(분)	승객 탑승	실내온도	희망온도
0	x	11	10
1	o	10	10
2	o	10	10
3	o	10	10
4	o	10	10
5	o	10	10
6	o	10	10
7	x	10	10
8	x	10	10
9	x	10	10
10	o	10	10
11	o	10	off
이때 총 소비전력은 20이며, 이보다 소비전력이 적어지는 방법은 없습니다. 따라서 20을 return 해야 합니다.

입출력 예 #4

3번째 예시와 비교했을 때 b의 값이 다릅니다. 아래 표와 같이 에어컨을 조작하면 소비전력이 최소가 됩니다.

시간(분)	승객 탑승	실내온도	희망온도
0	x	11	8
1	o	10	8
2	o	9	8
3	o	8	off
4	o	9	off
5	o	10	8
6	o	9	off
7	x	10	off
8	x	11	off
9	x	11	9
10	o	10	9
11	o	9	off
이때 총 소비전력은 60이며, 이보다 소비전력이 적어지는 방법은 없습니다. 따라서 60을 return 해야 합니다.

t1 ~ t2는 t1도 이상 t2도 이하의 온도 범위를 나타냅니다.
'''

def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    return answer


