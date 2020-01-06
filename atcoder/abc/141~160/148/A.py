
def main():
    A = int(input())
    B = int(input())
    now = set([1,2,3])
    now.discard(A)
    now.discard(B)
    print(now.pop())

if __name__ == "__main__":
    main()    