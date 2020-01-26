def main():
    N,M = map(int,input().split())
    disc_ls = [int(input()) for _ in range(M)]
    ans = [int(i)+1 for i in range(N)]
    now = 0
    for i in disc_ls:
        if now == i:
            continue
        for j in range(N):
            if i==ans[j]:
                index=j
        
        ans[index] = now
        now = i
    for i in ans:
        print(i)


if __name__ == "__main__":
    main()