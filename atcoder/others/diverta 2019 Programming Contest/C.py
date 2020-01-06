
def main():
    N = int(input())
    cnt = 0
    ab,a,b = 0,0,0
    for _ in range(N):
        s = input()
        for i in range(len(s)-1):
            if s[i:i+2]=="AB":
                cnt += 1
        if s[0]=="B" and s[-1]=="A":
            ab += 1
        elif s[0]=="B":
            b +=1
        elif s[-1]=="A":
            a +=1

    if ab==0:
        print(cnt+min(a,b))
    else:
        if a+b==0:
            print(cnt+ab-1)
        else:
            print(cnt+ab+min(a,b))

if __name__ == "__main__":
    main()