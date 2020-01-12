from collections import defaultdict
def main():
    dic = defaultdict(int)
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for i,s in enumerate(ascii_lowercase):
        dic[s] = i
    inp = input()
    idx = dic[inp] + 1
    print(ascii_lowercase[idx])
if __name__ == '__main__':
    main()