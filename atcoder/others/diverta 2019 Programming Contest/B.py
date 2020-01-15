def main():
    R,G,B,N = map(int,input().split())
    ans = 0
    for i in range(N//R+1):
        for j in range(N//G+1):
            now = N - R*i - G*j
            if now%B==0 and now>=0:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()