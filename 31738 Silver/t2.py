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