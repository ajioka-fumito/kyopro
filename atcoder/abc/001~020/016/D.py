def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 and td1*td2<0

def main():
    A_x,A_y,B_x,B_y = map(int,input().split())
    p1,p2 = [A_x,A_y],[B_x,B_y]
    N = int(input())
    points = [[int(x) for x in input().split()] for _ in range(N)]
    points.append(points[0])
    ans = 0
    for i in range(N):
        ans += int(intersect(p1,p2,points[i],points[i+1]))
    print(ans//2+1)
if __name__ == "__main__":
    main()