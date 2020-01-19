def main():
    a,b = map(int,input().split())
    ans1 = str(a)*b
    ans2 = str(b)*a
    ls = [ans1,ans2]
    ls = sorted(ls)
    print(ls[0])
if __name__ == '__main__':
    main()