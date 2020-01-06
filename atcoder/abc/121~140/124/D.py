def main():
    n,k = map(int,input().split())
    s = list(input())
    ls = [[],[]]
    if s[0]=="1":
        flg = 1
    else:
        flg = 0

    now = 1
    for i in range(1,n):

        if s[i] == str(flg):
            now += 1
        else:
            ls[0].append(flg)
            if flg==1:
                flg = 0
            else:
                flg = 1
            ls[1].append(now)
            now = 1
    ls[0].append(flg)
    ls[1].append(now)
    print(ls)
    ls_cumsum = [0]
    for i in range(len(ls[1])):
        ls_cumsum.append(ls_cumsum[-1]+ls[1][i])
    print(ls_cumsum)

    ans = []
    for i in range(len(ls[0])-k+1):
        print(i)
        if ls[0][i]==0:
            ans.append(ls_cumsum[i+k+1]-ls_cumsum[i])
        else:
            try:
                ans.append(ls_cumsum[i+2*k+1]-ls_cumsum[i])
            except:
                break
    print(max(ans))
    
if __name__ == "__main__":
    main()