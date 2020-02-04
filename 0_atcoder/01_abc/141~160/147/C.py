import sys
input = sys.stdin.readline
def main():
    n = int(input())
    ls = [[] for _ in range(n)]
    ls_a = []
    for i in range(n):
        a = int(input())
        ls_a.append(a)
        for _ in range(a):
            x,y = map(int,input().split())
            ls[i].append([x,y])
    ans = -1
    for i in range(2**n):
        can = [0 for _ in range(n)]
        for j in range(n):
            if (i >> j)&1:
                can[j] = 1
                
        flg = True
        for j in range(n):
            for k in range(ls_a[j]):
                now = ls[j][k]
                if can[j]==1:
                    if can[now[0]-1]==now[1]:
                        pass
                    else:
                        flg = False
                else:
                    if can[now[0]-1]==now[1]:
                        flg = False
                    else:
                        pass

        if flg==True:
            ans = max(ans,sum(can))
        else:
            pass

    if ans!= -1:
        print(ans)
    else:
        print(0)

if __name__ == "__main__":
    main()