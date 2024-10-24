# 괄호를 넣어서 식의 값을 최소로 만들어야하는 문제
# 그렇다면 어떻게 해야 최소로 만들 수 있을까?
# 바로 -가 오면 괄호로 묶어서 음의 값을 최대로 만들면 최소의 값이 나오지 않을까?
# 예를 들어 55-50+40 을 최소로 만들기 위해서는 55-(50+40) 즉 -35가 최소이지 않을까?

formula = str(input())
part = formula.split('-')

print(formula)
print(part)
ans = 0

# 처음이 음수일 수도 있으니까 
x = sum(map(int,(part[0].split('+'))))
if formula[0] == '-':
    ans -= x 
else: 
    ans += x

for x in part[1:]:
    x = sum(map(int,(x.split('+'))))
    print('x = ',x)
    ans -= x

print(ans)