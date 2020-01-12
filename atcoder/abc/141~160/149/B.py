def main():
    A,B,K = map(int,input().split())
    # 1
    if A>=K:
        print(A-K,B)
    else:
        print(0,max(B-(K-A),0))

    
if __name__ == '__main__':
    main()