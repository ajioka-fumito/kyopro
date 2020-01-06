def main():
    N = int(input())
    S = input()

    L,R = "(",")"
    first_L,first_R = -1,-1
    last_L,last_R = -1,-1
    cnt_L,cnt_R = 0,0
    for i in range(len(S)):
        if S[i]==L:
            last_L = i
            if first_L==-1:
                first_L=i
            cnt_L += 1


        else:
            last_R=i
            if first_R==-1:
                first_R=i
            cnt_R += 1

    if cnt_L == 0:
        S  = "("*cnt_R + S
        print(S)
    elif cnt_R == 0:
        S  = S + ")"*cnt_L
        print(S)

    else:
        cnt = 0
        for i in range(first_L,N):
            if S[i]==")":
                cnt +=1
        right_sub = ")"*max((cnt_L-cnt),0)
        cnt = 0
        for i in range(0,last_R+1):
            if S[i]=="(":
                cnt +=1
        left_sub = "("*max(0,(cnt_R-cnt))
        print(left_sub+S+right_sub)
        


if __name__ == "__main__":
    main()