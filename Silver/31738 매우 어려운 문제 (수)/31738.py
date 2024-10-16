# 문제 해결에 필요한 생각
# n은 10^18 까지 들어올 수 있으므로 Brute Force는 물론 DP로도 시간초과
# 그러므로 수학을 이용해서 n이 m보다 큰 경우 당연히 나누어 떨어지는 것과
# n부터 1까지 하니씩 곱하고 m으로 나눠보면서 나머지가 0일 떄 break 하는 것 
n,m = map(int,input().split())

tmp=1

if(n>=m):
    print(0)
else:
    for i in range(n,0,-1):
        tmp*=i
        tmp%=m

        if(tmp==0):
            break; 
            
    print(tmp)