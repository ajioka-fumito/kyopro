def main():
    s = input()
    s1 = s[0:4]
    s2 = s[4:]
    s = [s1," ",s2]
    print("".join(s))
if __name__ == '__main__':
    main()