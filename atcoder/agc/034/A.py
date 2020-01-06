
def main():
    N,A,B,C,D = map(int,input().split())
    S = list(input())
    # check 1
    check = S[B:D-1]
    flg=False
    for i in check:
        if i=="#":
            if flg:
                print("No")
                exit()
            else:
                flg=True
        else:
            if flg:
                flg=False
            else:
                pass
            
    check = S[A:C-1]
    flg = False
    for i in check:
        if i == "#":
            if flg:
                print("No")
                exit()
            else:
                flg=True
        else:
            if flg:
                flg=False
            else:
                pass

    # check 2
    if D>C:
        print("Yes")
        exit()
    else:
        pass
    # check 3
    check = S[A:C-1]
    cnt = 0
    for i in check:
        if i == ".":
            cnt += 1
        else:
            cnt = 0

        if cnt == 3:
            print("Yes")
            exit()
    print("No")
if __name__ == "__main__":
    main()