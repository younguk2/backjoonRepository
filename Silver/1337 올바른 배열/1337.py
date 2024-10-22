# 배열 안의 원소 중 5개가 연속적으로 만들기 위해 추가 원소의 최소 개수
# 각 원소들 +- 5 내의 최대값
# 1) 5개 미만일 경우 
# 2) 5개 이상일 경우 
# 배열 안의 원소 중 5개가 연속적으로 만들기 위해 추가 원소의 최소 개수

n = int(input())
data = []

for i in range(n):
    m = int(input())
    data.append(m)

data.sort()

toAdd = 5
for i in range(n):
    cnt = 0
    for j in range(data[i],data[i]+5):
        if j not in data:
            cnt+=1
    toAdd = min(toAdd,cnt)
print(toAdd)
