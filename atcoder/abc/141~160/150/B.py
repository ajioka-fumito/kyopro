def main():
    N = int(input())
    S = input()
    ls = []
    for i in range(N-2):
        if S[i]=="A":
            ls.append(i)

    ans = 0
    for i in ls:
        if S[i:i+3]=="ABC":
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()