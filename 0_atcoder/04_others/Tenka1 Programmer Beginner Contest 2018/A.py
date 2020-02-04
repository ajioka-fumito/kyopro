def main():
    ls = list(input())
    ans = 0
    for i in range(len(ls)):
        if ls[i]=="1":
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()