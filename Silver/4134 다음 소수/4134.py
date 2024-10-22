# 입력한 수보다 크거나 같은 숫자 중 가장 작은 숫자를 찾는 문제
# 1. 소수 찾기 알고리즘은 제곱근을 활용하여 소수 판별
# 2. 입력받은 수를 소수인지 판별하고 맞다면 해당 수를 출력
# 3. 만약 입력받은 수가 소수가 아니라면 해당 수에 +1 하고 판별하는 것을 반복
import math 

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())

for i in range(n):
    k = int(input())

    while True:
        if prime(k):
            print(k)
            break
        else:
            k += 1
