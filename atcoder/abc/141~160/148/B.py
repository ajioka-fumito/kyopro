
def main():
    N = int(input())
    s,t = [x for x in input().split()]

    ans = ""

    for i in range(N):
        ans += s[i]
        ans += t[i]

    print(ans)
if __name__ == "__main__":
    main()    