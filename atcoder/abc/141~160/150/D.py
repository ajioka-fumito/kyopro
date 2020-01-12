import fractions
def main():
    N,M = map(int,input().split())
    A = [int(x)//2 for x in input().split()]
    # check
    ls = []
    for i in range(N):
        now = A[i]
        cnt = 0
        while 1:
            if now%2==0:
                now = now//2
                cnt +=1
            else:
                ls.append(cnt)
                break

    ls = set(ls)
    if len(ls)!=1:
        print(0)
        exit()


    sub = A[0]
    for i in range(1,N):
        sub = sub*A[i]//fractions.gcd(sub,A[i])
    B = M//sub
    print((B-1)//2+1)
if __name__ == '__main__':
    main()