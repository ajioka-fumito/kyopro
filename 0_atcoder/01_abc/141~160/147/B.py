def main():
    s = list(input())
    lenth = len(s)
    ans = 0
    for i in range(lenth//2):
        if s[i]==s[len(s)-1-i]:
            pass
        else:
            ans+=1
    print(ans)
if __name__ == "__main__":
    main()