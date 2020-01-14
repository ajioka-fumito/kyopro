def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        idx = -1
        for i in range(n):
            if s[i]=="A":
                idx = i
                break
        if idx==-1:
            print(0)
            continue
        ans = 0
        ls = []
        for i in range(idx,n):
            if s[i]=="A":
                ans = 0
            else:
                ans += 1

            ls.append(ans)
        print(max(ls))

if __name__ == '__main__':
    main()
