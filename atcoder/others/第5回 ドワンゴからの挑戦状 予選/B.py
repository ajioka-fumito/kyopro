def main():
    N,K = map(int,input().split())
    A = [int(x) for x in input().split()]
    A_cumsum = [0]
    for i in range(0,N):
        A_cumsum.append(A_cumsum[-1]+A[i])
    
    digit = len(bin(sum(A)))-2

    ls = []
    for i in range(N+1):
        for j in range(i+1,N+1):
            now = bin(A_cumsum[j]-A_cumsum[i])[2:]
            now = "0"*(digit-len(now))+now
            ls.append(now)
    
    ans = [0 for _ in range(digit)]

    for i in range(digit):
        
        now = []
        for j in range(len(ls)):
            if ls[j][i]=="1":
                now.append(ls[j])
        if K<=len(now):
            ls = now
            ans[i]=1
    out = ""
    for i in ans:
        out += str(i)
    print(int(out,2))

    
        
if __name__ == '__main__':
    main()