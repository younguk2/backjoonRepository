#크로아티아 알파뱃 
inStr=list(map(str,input()))
cnt=0
for i in range(len(inStr)-1,-1,-1):
    if(ord(inStr[i])>=97 and ord(inStr[i])<=122):
        cnt+=1
    if inStr[i]=="=":
        if inStr[i-1]=="z":
            if inStr[i-2]=="d":
                cnt-=1
    elif inStr[i]=="j":
        if inStr[i-1]=="n" or inStr[i-1]=="l":
            cnt-=1
print(str(cnt),sep="\n")

