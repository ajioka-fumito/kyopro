from collections import defaultdict
def main():
    dict_A = defaultdict(int)
    dict_B = defaultdict(int)
    N = int(input())

    now = input()
    dict_A[now] += 1
    flg = 1

    

    for _ in range(N-1):
        next_ = input()

        if flg==1:
            if dict_B[next_]==0 and now[-1]==now[0]:
                flg *= -1
                dict_B[next_]+=1
                now = next_
            else:
                print("WIN")
                exit()
        else:
            if dict_A[next_]==0 and now[-1]==now[0]:
                flg *= -1
                dict_A[next_]+=1
                now = next_
            else:
                print("LOSE")
                exit()

    print("DRAW")





if __name__ == "__main__":
    main()    