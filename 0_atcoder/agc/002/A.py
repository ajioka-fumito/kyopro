from collections import defaultdict

def main():
    N,M = map(int,input().split())
    move = [[int(x) for x in input().split()] for _ in range(M)]
    box = defaultdict(int)
    for i in range(N):
        box[i+1] = 1
    
    for (b,a) in move:
        box[b] -= 1
        box[a] += 1

    print(box) 


        
    
if __name__ == "__main__":
    main()    