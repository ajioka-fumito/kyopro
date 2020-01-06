
def Sum(N):
    return N*(N+1)//2

def main():
    S = input()
    ls = []

    now = []
    if S[0]=="<":
        now = ["<",1]
    else:
        now = [">",1]

    for i in range(1,len(S)):
        if S[i]==now[0]:
            now = [now[0],now[1]+1]
        else:
            ls.append(now)
            now = [S[i],1]
    ls.append(now)
    
    ans = 0
    now = 0
    while 1:
        
        if ls[now][0]=="<":





if __name__ == "__main__":
    main()