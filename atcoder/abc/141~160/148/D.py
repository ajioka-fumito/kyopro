
def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    now = 0
    for i in range(N):
        if A[i]==now+1:
            now +=1
        else:
            pass
    if now == 0:
        print(-1)
    else:
        print(N-now)
if __name__ == "__main__":
    main()    