
def solve(digits):
    ans = 0
    # 5
    for i in range(1,digits):
        ans += 10**(digits-1-i)
    return ans

def main():
    N = []
    for x in list(input()):
        N.insert(0,x)
    ans = 0

    for i in range(len(N)):
        ans += int(N[i])*solve(i+1)
        

    print(ans)



if __name__ == "__main__":
    main()    