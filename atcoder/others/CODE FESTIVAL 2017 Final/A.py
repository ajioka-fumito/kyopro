def main():
    S = input()
    if len(S)>10:
        print("NO")
        exit()
    string = "AKIHABARA"

    # check 1
    check = ""
    for i in S:
        if i == "A":
            pass
        else:
            check += i
    if check == "KIHBR":
        pass
    else:
        print("NO")
        exit()

    flg = False

    for i in S:
        if i == "A":
            if flg:
                print("NO")
                exit()
            else:
                flg = True
        else:
            if flg:
                flg = False
            else:
                pass
    print("YES")

if __name__ == "__main__":
    main()