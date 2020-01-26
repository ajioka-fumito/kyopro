from collections import defaultdict
def main():
    N = int(input())
    set = defaultdict(int)
    
    now = input()
    set[now] = 1
    last = now[-1]
    for i in range(N-1):
        now = input()
        if i%2==0:
            if set[now]!=0 or now[0]!=last:
                print("WIN")
                exit()
            else:
                set[now] = 1
                last = now[-1]
                
        else:
            if set[now]!=0 or now[0]!=last:
                print("LOSE")
                exit()
            else:
                set[now] = 1
                last = now[-1]

    print("DRAW")
        

if __name__ == '__main__':
    main()