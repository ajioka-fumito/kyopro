def main():
    N = int(input())
    ls = [0]
    ans = []

    for i in range(1,N+1):
        ls.append(ls[-1]+i)
        ans.append(i)
        if N<=ls[-1]:
            break
                
    for i in range(len(ans)):
        if ans[i]==(ls[-1]-N):
            pass
        else:
            print(ans[i])

if __name__ == '__main__':
    main()