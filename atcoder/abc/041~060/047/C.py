def main():
    s = input()
    now = s[0]
    ans = 0
    for i in range(1,len(s)):
        if now==s[i]:
            pass
        else:
            now = s[i]
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()