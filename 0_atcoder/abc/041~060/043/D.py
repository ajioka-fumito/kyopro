def main():
    s = input()
    b1,b2 = s[1],s[0]
    if len(s)==2:
        if b1 == b2:
            print("1 2")
            exit()
        else:
            print("-1 -1")
            exit()
    for i in range(2,len(s)):
        if s[i] == b1 or s[i] == b2:
            print("{} {}".format(i-1,i+1))
            exit()
        else:
            b1,b2 = s[i],s[i-1] 
    print("-1 -1")

if __name__=='__main__':
    main()