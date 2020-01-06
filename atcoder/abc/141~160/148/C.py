import fractions
def main():
    A,B = map(int,input().split())
    g = fractions.gcd(A,B)
    print(A*B//g)
if __name__ == "__main__":
    main()    