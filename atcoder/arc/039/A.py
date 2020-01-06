import copy
def main():
    a,b = map(str,input().split())
    A = list(a+b)
    ans = -1*float("inf")
    for i in range(6):
        for j in range(10):
            if (i == 0 or i == 3) and j == 0:
                pass
            else:
                can = copy.deepcopy(A)
                can[i] = str(j)
                ans = max(ans,int("".join(can[:3]))-int("".join(can[3:])))
    print(ans)

if __name__ == "__main__":
    main()