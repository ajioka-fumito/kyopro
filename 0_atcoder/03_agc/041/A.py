def main():
    N,A,B = map(int,input().split())
    if abs(A-B)%2==1:
        print(min(A-1,N-B)+1+(B-A-1)//2)
    else:
        print(abs(A-B)//2)

if __name__ == '__main__':
    main()