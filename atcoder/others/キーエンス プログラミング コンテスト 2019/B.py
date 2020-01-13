from copy import deepcopy
def main():
    S = list(input())

    for i in range(len(S)):
        for j in range(i,len(S)+1):
            now = deepcopy(S)
            del now[i:j]
            if "".join(now)=="keyence":
                print("YES")
                exit()
    print("NO")
if __name__ == '__main__':
    main()