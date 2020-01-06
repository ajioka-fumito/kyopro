import math
def main():
    N = int(input())
    for i in range(50000):
        ans = math.floor(i*1.08)
        if ans == N:
            print(i)
            exit()
    print(":(")
if __name__ == "__main__":
    main()