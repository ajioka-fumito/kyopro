def main():
    N,A,B = map(int,input().split())
    S = input()
    now = 0
    others = 0
    ans = []

    for i in S:

        if i == "a":
            if now < A+B:
                ans.append("Yes")
                now +=1
            else:
                ans.append("No")
        elif i=="b":
            others += 1
            if now < A+B and others<=B:
                ans.append("Yes")
                now += 1
            else:
                ans.append("No")
        else:
            ans.append("No")
    for i in ans:
        print(i)        
if __name__ == '__main__':
    main()