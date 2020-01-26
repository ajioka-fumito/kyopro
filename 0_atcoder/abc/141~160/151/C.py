
def main():
    N,M = map(int,input().split())
    P,S = [],[]
    for _ in range(M):
        p,s = map(str,input().split())
        p = int(p)
        P.append(p)
        S.append(s)
    AC = [0 for i in range(N+1)]
    for i in range(M):
        if S[i]=="AC" and AC[P[i]]==0:
            AC[P[i]] += 1
        else:
            pass
    
    WA = [0 for i in range(N+1)]
    WA_flg = [ False for _ in range(N+1)]
    for i in range(M):
        if AC[P[i]]==0:
            pass
        else:
            if WA_flg[P[i]]==True:
                pass
            else:
                if S[i] == "AC":
                    WA_flg[P[i]]=True
                else:
                    WA[P[i]] += 1

    print(sum(AC),end=" ")
    print(sum(WA))

if __name__ == '__main__':
    main()