def main():
    n = int(input())
    s = input()
    ls_first = [-1 for _ in range(10)]
    ls_last = [-1 for _ in range(10)]


    for i,now in enumerate(s):
        ls_last[int(now)] = i
        if ls_first[int(now)] == -1:
            ls_first[int(now)] = i

    ans = 0
    for i in range(10):
        for j in range(10):
            if ls_first[i]==-1 or ls_last[j]==-1:
                pass
            else:
                now = set([])
                for k in range(ls_first[i]+1,ls_last[j]):
                    now.add(int(s[k]))
                ans += len(now)
    print(ans)    


if __name__ == "__main__":
    main()