for i in range(int(input())):
    k = int(input())
    n = int(input())
    ans = [list(range(n+1))]
    for j in range(k+1):
        floor2add = []
        for l in range(n+1):
            floor2add.append(sum(ans[-1][:l+1]))
        ans.append(floor2add)
    print(ans[k][n])
