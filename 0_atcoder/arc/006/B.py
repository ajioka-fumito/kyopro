def check(N,ls,index):
    if index==0:
        if ls[index+1]=="-":
            return index+2
        else:
            return index
    elif index == 2*N-2:
        if ls[index-1]=="-":
            return index-2
        else:
            return index
    else:
        if ls[index-1]=="-":
            return index-2
        elif ls[index+1]=="-":
            return index+2
        else:
            return index

def main():
    N,L = map(int,input().split())
    ls = []
    for _ in range(L):
        ls.append(input())
    goal = input()

    index = 0
    for i,now in enumerate(goal):
        if now=="o":
            index = i

    now = L-1

    while 1:

        index = check(N,ls[now],index)

if __name__ == "__main__":
    main()