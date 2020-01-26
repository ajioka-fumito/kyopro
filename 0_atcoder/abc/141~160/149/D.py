def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    dic = {"r":P,"s":R,"p":S}
    T = list(input())
    ans = 0
    for i in range(K):   
        for j in range(i,N,K):
            if j == i:
                ans += dic[T[j]]
            else:
                if T[j-K]==T[j]:
                    T[j]="x"
                else:
                    ans += dic[T[j]]
    print(ans)
        
if __name__ == '__main__':
    main()