def main():
    N = int(input())
    s = input()
    l,r = 0,0
    for i in range(N):
        if s[i]=="L":
            l += 1
        else:
            r += 1
    print(l+r+1)
if __name__ == '__main__':
    main()