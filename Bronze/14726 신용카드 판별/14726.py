n = int(input())

for _ in range(n):
    cardNum = int(input())
    cardNum = [int(digit) for digit in str(cardNum)]

    for i in range(len(cardNum) - 1, -1, -1):
        if (len(cardNum) - i) % 2 == 0:
            # 짝수 자리 수 (0-indexed에서 홀수 번째)
            cardNum[i] *= 2
            if cardNum[i] >= 10:
                # 각 자리의 숫자를 더함
                cardNum[i] = cardNum[i] // 10 + cardNum[i] % 10

    if sum(cardNum) % 10 == 0:
        print('T')  # 유효한 카드
    else:
        print('F')  # 유효하지 않은 카드
