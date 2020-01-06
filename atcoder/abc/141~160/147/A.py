import sys
input = sys.stdin.readline
def main():
    a = [int(x) for x in input().split()]
    a = sum(a)
    if a>=22:
        print("bust")
    else:
        print("win")
if __name__ == "__main__":
    main()