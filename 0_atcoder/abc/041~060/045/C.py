import math

def flg(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

def main():
    n = int(input())
    ls = [[int(x) for x in input().split()] for _ in range(n)]
    t,a = ls[0]
    flg_now = flg(t,a)
    for i in range(1,n):
        nex = ls[i]
        flg_nex = flg(nex[0],nex[1])
        if flg_nex==0:
            t = max(a,t)
            a = max(a,t)
        else:
            if flg_now==flg_nex:
                if flg_now==1:
                    t = math.ceil(t/nex[0])*nex[0]
                    a = math.ceil(t/nex[0])*nex[1]
                elif flg_now==-1:
                    a = math.ceil(t/nex[1])*nex[1]
                    t = math.ceil(t/nex[1])*nex[0]         
            else:
                if flg_now==1:
                    t = math.ceil(t/nex[0])*nex[0]
                    a = t*nex[1]//nex[0]
                elif flg_now==0:
                    if flg_nex==1:
                            a = math.ceil(a/nex[1])*nex[1]
                            t = math.ceil(a/nex[1])*nex[0]
                    else:
                        t = math.ceil(t/nex[0])*nex[0]
                        a = math.ceil(t/nex[0])*nex[1]
                else:
                    a = math.ceil(a/nex[1])*nex[1]
                    t = a*nex[0]//nex[1]
        flg_now = flg(nex[0],nex[1])
    print(a+t)

if __name__ == "__main__":
    main()