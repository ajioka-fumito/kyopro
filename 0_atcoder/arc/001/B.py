
def solve(n):
    if n==5 or n==1:
        return 1
    elif n==4 or n==2:
        return 2
    elif n==3:
        return 3
    elif n==0:
        return 0
    else:
        return solve(n-5)+1
    

def main():
    A,B = map(int,input().split())
    sub = abs(A-B)  

    # sub 1
    ans1 = sub//10
    sub1 = sub%10

    # sub2
    ans2 = ans1+1
    sub2 = 10-sub1

    ans1 += solve(sub1)
    ans2 += solve(sub2)

    print(min(ans1,ans2))


if __name__=="__main__":
    main()