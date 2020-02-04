import math 
def main():
    X = int(input())
    a = math.ceil(X/105)
    b = 105*a-X
    i = 0
    while 1:
        if b>5:
            b-=5
            i+=1 
        else:
            if b==0:
                break
            else:
                i+=1
                break
    if a<i:
        print(0)
    else:
        print(1)

                
if __name__ == "__main__":
    main()