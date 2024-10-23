# 수 정렬의 조건에서 입력받은 수가 10000 이하의 자연수이기에
# 0~10000 의 배열을 만들고 입력받은 수를 +1 해줌
# 마지막으로 num_list(0~10000 배열)을 인덱스 순서대로 1 이상인 경우 그 값에 따라 출력을 해줌
import sys

n = int(sys.stdin.readline())

num_list = [0]*10001

for i in range(n):
    k = int(sys.stdin.readline())
    num_list[k] += 1

for i in range(len(num_list)):
    if(num_list[i] >= 1):
        for j in range(0,num_list[i]):
            print(i)