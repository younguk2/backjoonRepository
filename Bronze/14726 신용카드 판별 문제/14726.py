# 16자리 신용카드의 유효성을 알아내는 단순한 문제 

n = int(input())

for _ in range(n):
    cardNum = int(input())
    cardNum = [int(digit) for digit in str(cardNum)]

    for i in range(len(cardNum) - 1, -1, -1):
        # 짝수 자리 (1-indexed에서 홀수 번째)
        if (len(cardNum) - i) % 2 == 0:
            cardNum[i] *= 2  # 짝수 자리 수를 두 배로
            
            # 10 이상인 경우 각 자리의 숫자를 더함 예를 들면 16 -> 7
            if cardNum[i] >= 10:
                cardNum[i] = cardNum[i] // 10 + cardNum[i] % 10
    
    # 최종 합 계산
    if sum(cardNum) % 10 == 0:
        print('T')  # 유효한 카드
    else:
        print('F')  # 유효하지 않은 카드
    
