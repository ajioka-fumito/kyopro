import sys

def main():
    N = int(input())
    #dic = dict(zip([int(x) for x in range(26)],[chr(i) for i in range(97,97+26)]))
    ls = []
    ls_rev = []
    for i in range(N):
        s = input()
        ls.append([i,s])
        ls_rev.append([i,s[::-1]])
    ls_rev = sorted(ls_rev,key= lambda x:x[1])
    for i,st in ls_rev:
        print(ls[i][1])

    
if __name__ == "__main__":
    main()