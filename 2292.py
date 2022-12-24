N = int(input())
ans=0
while True:
    ans+=1
    if 3*ans*ans-9*ans+2<=N and N<=3*ans*ans-3*ans+1:
        print(ans)
        exit()