import math

def red(x1,y1,r,x,y):
    dis = math.sqrt((x1-x)**2+(y1-y)**2)
    if dis<=r:
        return True
    else:
        return False

def blue(x2,y2,x3,y3,x,y):
    if x2<=x<=x3 and y2<=y<=y3:
        return True
    else:
        return False

def main():
    x1,y1,r = map(int,input().split())
    x2,y2,x3,y3 = map(int,input().split())

    B,R = False,False
    for x in range(-100,101):
        for y in range(-100,101):
            if red(x1,y1,r,x,y)==True and blue(x2,y2,x3,y3,x,y)==False:
                R = True
            if red(x1,y1,r,x,y)==False and blue(x2,y2,x3,y3,x,y)==True:
                B = True
    
    if R:
        print("YES")
    else:
        print("NO")

    if B:
        print("YES")
    else:
        print("NO")

        
if __name__ == "__main__":
    main()